FROM python:3.8.10-slim

WORKDIR /backend

COPY . /backend

RUN pip install -r requirements.txt

CMD uvicorn main:app --port=8000 --host=0.0.0.0