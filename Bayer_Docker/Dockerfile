FROM python:3.6
LABEL maintainer = cgriso@siue.edu

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN python -m nltk.downloader 'punkt'

                