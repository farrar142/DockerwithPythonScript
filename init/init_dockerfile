FROM python:3.10

LABEL Farrar142 "gksdjf1690@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY wait.sh .
COPY requirements.txt .
#COPY . .

RUN pip3 install -r requirements.txt \
    && apt-get update \
    && apt-get install netcat-openbsd -y

ENTRYPOINT python manage.py runserver 0.0.0.0:8000