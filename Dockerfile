FROM python:3.12-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src/ ./

ENV DJANGO_SETTINGS_MODULE='config.settings'

EXPOSE 8000