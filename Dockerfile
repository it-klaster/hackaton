FROM node:latest

RUN mkdir -p /app
WORKDIR /app

COPY package.json ./

RUN npm install --save-dev
COPY . /app


