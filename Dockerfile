FROM python:3.9-buster
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt