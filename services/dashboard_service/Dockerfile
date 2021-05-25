FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

ENV ACCOUNTID=710349444454

COPY src/   ./