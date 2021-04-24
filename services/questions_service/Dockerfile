FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

ENV TABLE=exam_question_files

COPY src/   ./