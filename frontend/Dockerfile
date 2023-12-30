FROM node:18-alpine

WORKDIR /frontend

ENV PATH /app/node_modules/.bin:$PATH

COPY . /frontend

RUN npm install
