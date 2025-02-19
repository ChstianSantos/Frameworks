FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]


#MySQL
#https://docs.docker.com/guides/databases/#run-a-local-containerized-database

# syntax=docker/dockerfile:1

# Use the base image mysql:latest
FROM mysql:latest

# Set environment variables
ENV MYSQL_DATABASE mydb

# Copy custom scripts or configuration files from your host to the container
COPY ./scripts/ /docker-entrypoint-initdb.d/