FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install -r requirements.txt
