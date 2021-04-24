FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

ENV ACCOUNTID=710349444454
ENV DASHBOARDID=b190d1bc-b011-4542-a640-994e3f4d3ba5

COPY src/   ./