from flask import Flask, request, jsonify,send_file,Response
import json
from PIL import Image 
# from celery import Celery
import base64
import io

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
    return "Ты пидор"

@app.route("/colorize", methods=["POST"])
def process_image():
    try:
        data = request.get_json(force=True)
        images=[]
        id=[]
        print(data)
        for i in data:
            imgdata = base64.b64decode(i['image'])
            stream = io.BytesIO(imgdata)
            image = Image.open(stream).convert("RGB")
            stream.close()
            images.append(image)
            id.append(i['id'])

        for index,img in enumerate(images):
            img.save("result/{}.jpg".format(index)) 

        return '200'
    except Exception as e:
        return str(e)

    



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
    