from flask import Flask, request, jsonify,send_file
import json
from PIL import Image 
import io
import requests
import base64
from deoldify import device
from deoldify._device import DeviceId
from deoldify.imgs_col import *
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")
# celery_app = Celery('server', backend='redis://127.0.0.1', broker='redis://127.0.0.1')  # и брокер и база - redis
app = Flask(__name__)


device.set(device=DeviceId.GPU0)
torch.backends.cudnn.benchmark=True
colorizer = get_image_colorizer()

render_factor=20

@app.route('/')  # Функция обработчик для /
def hello():
    return "Hello, from Flask"


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
    print(images)
    for index,img in enumerate(images):
        result=colorizer.get_transformed_image(img, render_factor)
        result.save("{}.jpg".format(index))

    return 'asd'# Кодируем ответ обратно в JSON

if __name__ == '__main__':
	# app.run(debug=True)
    app.run("0.0.0.0", 8000)  # Запускаем сервер на 8000 порту
    