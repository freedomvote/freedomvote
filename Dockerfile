FROM python:2.7-onbuild
RUN apt-get update && apt-get install -y gettext
