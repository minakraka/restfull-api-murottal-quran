FROM python:3.7.9

RUN apt-get update && apt-get install
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD . /code/

WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /code
