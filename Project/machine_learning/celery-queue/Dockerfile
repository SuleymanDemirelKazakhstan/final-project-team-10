FROM python:3.6

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

COPY . /queue
WORKDIR /queue

RUN pip install -r requirements.txt

# production
ENTRYPOINT celery -A tasks worker --loglevel=info  -c 1