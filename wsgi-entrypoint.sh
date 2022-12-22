#!/bin/sh

until cd /app/

do
    echo "Waiting for server volume..."
done

until alembic upgrade head

do
    echo "Waiting for db to be ready..."
    sleep 2
done

uvicorn main:app --host 0.0.0.0 --port 80