FROM python:3.5
ENV PYTHONUNBUFFERED 1
ENV CHAT_APP_ENV development_docker
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r server/misc/requirements.txt
