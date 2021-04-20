import os
import time
from celery import Celery
import io
import base64
from deoldify import device
from deoldify._device import DeviceId
from deoldify.imgs_col import *
import warnings
from PIL import Image 
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

device.set(device=DeviceId.CPU)
torch.backends.cudnn.benchmark=True
colorizer = get_image_colorizer()
render_factor=20


@celery.task(name='tasks.colorize')
def colorize(data):
    email=data['email']
    data=data['data']
    images=[]
    id=[]
    for i in data:
        imgdata = base64.b64decode(i['image'])
        stream = io.BytesIO(imgdata)
        image = Image.open(stream).convert("RGB")
        stream.close()
        images.append(image)
        id.append(i['id'])

    images_res=[]
    for index,img in enumerate(images):
        img=colorizer.get_transformed_image(img, render_factor)
        img.save("result/{}.jpg".format(id[index]))   
        im_file = BytesIO()
        img.save(im_file, format="JPEG")
        im_bytes = im_file.getvalue() 
        im_b64 = base64.b64encode(im_bytes)
        img=im_b64.decode("utf-8")
        images_res.append(img)
    json={
    "readyData": images_res
     
    }
    requests.put('http://192.168.1.208:8080/api/photosDone/{}'.format(email),json=json)
    return 'done'
