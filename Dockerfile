FROM python:3.8.10-slim

WORKDIR /app

COPY . /app

RUN pip install -r ./fastapi/requirements.txt

CMD cd ./fastapi && uvicorn main:app --port=8000 --host=0.0.0.0