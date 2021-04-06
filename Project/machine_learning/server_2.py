from flask import Flask, request, jsonify
import json
from PIL import Image 
import io
import base64
from deoldify import device
from deoldify._device import DeviceId
from deoldify.imgs_col import *
import warnings
from celery import Celery
from celery.result import AsyncResult
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")


celery_app = Celery('server', backend='redis://localhost:6379', broker='redis://localhost:6379')  # и брокер и база - redis
app = Flask(__name__)


device.set(device=DeviceId.CPU)
torch.backends.cudnn.benchmark=True
colorizer = get_image_colorizer()
render_factor=20


@app.route('/')  # Функция обработчик для /
def hello():
    return "Hello, from Flask"

@celery_app.task
def colorize(images):
    res=len(images)
    for index,img in enumerate(images):
        colorizer.get_transformed_image(img, render_factor).save("{}.jpg".format(index))   
    return res


@app.route("/colorize", methods=["POST"])
def process_image():
    data = request.get_json(force=True)
    images=[]
    id=[]
    for i in data:
        imgdata = base64.b64decode(i['image'])
        stream = io.BytesIO(imgdata)
        image = Image.open(stream).convert("RGBA")
        stream.close()
        images.append(image)
        id.append(i['id'])

    task = colorize.delay(images) 
    response = {
        "task_id": str(task.id)
    }
    return json.dumps(response)



@app.route('/colorize/<task_id>')
def frequency_check_handler(task_id):
    task = AsyncResult(task_id, app=celery_app)
    if task.ready():
        response = {
            "status": "DONE",
            "result": task.result
        }
    else:
        response = {
            "status": "IN_PROGRESS"
        }
    return json.dumps(response)



if __name__ == '__main__':
	# app.run(debug=True)
    app.run("0.0.0.0", 8000)  # Запускаем сервер на 8000 порту
    