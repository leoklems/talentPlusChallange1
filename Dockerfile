FROM python:3.9-alpine
MAINTAINER Leoklems

ENV DHome=/app

RUN mkdir -p $DHome
WORKDIR $DHome

ENV PYTHONUNBUFFERED 1

COPY . $DHome
RUN pip install -r /requirements.txt

RUN adduser -D user
USER user

EXPOSE 8000
# minikube start --no-vtx-check --kubernetes-version=v1.23.3
