FROM		python:3.9-alpine
MAINTAINER	googie

ENV			PYTHONBUFFERD 1

COPY		./requirements.txt /requirements.txt
RUN			pip install -r /requirements.txt

RUN			mkdir /kyeolle
WORKDIR		/kyeolle
COPY		./kyeolle /kyeolle

RUN			adduser -D user
user		user
