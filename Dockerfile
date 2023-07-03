FROM python:3.11.4-alpine

ENV PYTHONUNBUFFERED 1
ENV GUNICORN_CMD_ARGS --bind=0.0.0.0:8000 --workers=3

COPY . /app/

RUN pip3 install --no-cache-dir -r /app/requirements.txt

WORKDIR /app/turizm