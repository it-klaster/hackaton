FROM python:latest

ENV PYTHONPATH=.

RUN mkdir -p /code
COPY . /code
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
