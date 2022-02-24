FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /homestay

ADD . /homestay

COPY ./requirements.txt /homestay/requirements.txt

RUN pip install -r requirements.txt

COPY . /homestay
