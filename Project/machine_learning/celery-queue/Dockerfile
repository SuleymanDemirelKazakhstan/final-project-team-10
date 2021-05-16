FROM python:3.6

ADD https://www.dropbox.com/s/usf7uifrctqw9rl/ColorizeStable_gen.pth?dl=1 models/ColorizeStable_gen.pth
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

COPY . /queue
WORKDIR /queue

ADD https://www.dropbox.com/s/usf7uifrctqw9rl/ColorizeStable_gen.pth?dl=1 models/ColorizeStable_gen.pth

RUN pip install -r requirements.txt

# production
ENTRYPOINT celery -A tasks worker --loglevel=info  -c 1