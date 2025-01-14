#!/bin/bash

sleep 15

alembic upgrade head

gunicorn backend.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000