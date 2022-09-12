#!/bin/bash

if [[ "$DB_ENGINE" =~ "postgres" ]]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

poetry run python manage.py migrate
poetry run python manage.py collectstatic

exec "$@"
