#!/bin/bash

sleep 15

celery --app=backend.tasks.celery_app:celery worker -l INFO -B
