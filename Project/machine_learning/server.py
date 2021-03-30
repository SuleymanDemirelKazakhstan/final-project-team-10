from flask import Flask, request, jsonify,send_file
import json
from PIL import Image 
from celery import Celery

# from deoldify import device
# from deoldify._device import DeviceId
# from deoldify.imgs_col import *

# celery_app = Celery('server', backend='redis://127.0.0.1', broker='redis://127.0.0.1')  # и брокер и база - redis
app = Flask(__name__)


# device.set(device=DeviceId.GPU0)
# torch.backends.cudnn.benchmark=True
# colorizer = get_image_colorizer()

# render_factor=13

@app.route('/')  # Функция обработчик для /
def hello():
    return "Hello, from Flask"

@app.route("/colorize", methods=["POST"])
def process_image():
    files = request.files.to_dict(flat=False)['image']
    # payload = request.form.to_dict()
    for i, file in enumerate(files):
        file.save(file.filename)
    # print(file.filename)
    
    # Read the image via file.stream
    # file.save(file.filename)

    img = Image.new(file.stream)


    return send_file(files, mimetype='image/gif')# Кодируем ответ обратно в JSON



    # files = request.files.to_dict(flat=False)['image']
    # for i, file in enumerate(files):
    #     file.save('res/{}'.format(file.filename))

    #     # print(type(img))
    #     # result = colorizer.get_transformed_image(img, render_factor)
    #     # print(result)
    #     # print(type())
    #     # response = {'name':file.name,'msg': 'success', 'size': [img.width, img.height]}
    #     return send_file(img, mimetype='image/gif') # Кодируем ответ обратно в JSON


if __name__ == '__main__':
	# app.run(debug=True)
    app.run("0.0.0.0", 8000)  # Запускаем сервер на 8000 порту
    