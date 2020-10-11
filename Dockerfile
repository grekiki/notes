FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

RUN apk --update add bash nano
ENV STATIC_PATH /app/
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt