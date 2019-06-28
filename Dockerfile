FROM python:3.7.0

RUN mkdir /catalog

COPY . /catalog

WORKDIR /catalog

RUN make setup
