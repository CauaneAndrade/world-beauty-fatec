FROM python:3.8-slim-buster

ARG APP_NAME
ARG ENVIRONMENT

ENV APP_NAME=${APP_NAME}
ENV ENVIRONMENT=${ENVIRONMENT}

ENV WORK_DIR=/usr/src/app
ENV REQUIREMENTS_DIR=/usr/src/requirements

WORKDIR ${WORK_DIR}

RUN mkdir /usr/src/requirements & apt-get update
# RUN apt install --qq -y build-essential

COPY ./requirements ${REQUIREMENTS_DIR}/
RUN pip install -r ${REQUIREMENTS_DIR}/${ENVIRONMENT}.txt

COPY ${APP_NAME}/ ${WORK_DIR}/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
