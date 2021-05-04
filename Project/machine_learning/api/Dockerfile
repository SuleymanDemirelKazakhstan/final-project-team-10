FROM python:3.6

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

ENV HOST 0.0.0.0
ENV PORT 8000
ENV DEBUG true

COPY . /api
WORKDIR /api

# install requirements
RUN pip install -r requirements.txt

# expose the app port
EXPOSE 8000

RUN pip install gunicorn

# run the app server in production with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "app:app"]

#gunicorn --bind 0.0.0.0:8000 --workers 3 app:app
#cd "ML & DS"/Diploma/docker-testing/api