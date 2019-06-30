FROM python:3.7.0

RUN apt-get update && apt-get install sudo

RUN mkdir /catalog

COPY . /catalog

WORKDIR /catalog

RUN make setup
