FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN apt-get update && apt-get install -y gettext
RUN pip install -r requirements.txt
