FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
RUN apt-get update && apt-get install -y gettext postgresql-client
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
ADD . /usr/src/app/
