# syntax=docker/dockerfile:1

# Creat workir app
FROM python:3.10-alpine3.15
WORKDIR /app/

# Install requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Add envirnoment variables
COPY ./.docker.env /app/.env

# Add migrations functional
COPY ./alembic.ini /app/alembic.ini
COPY ./alembic /app/alembic

# Add source app
COPY ./src /app/src
COPY ./manage.py /app/manage.py

COPY ./run-app.sh /app/run-app.sh
RUN chmod u+x /app/run-app.sh

CMD [ "/bin/sh", "./run-app.sh" ]

