FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
RUN apt-get update && apt-get install -y gettext postgresql-client
RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -P /usr/bin
RUN chmod +x /usr/bin/wait-for-it.sh
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /usr/src/app/
