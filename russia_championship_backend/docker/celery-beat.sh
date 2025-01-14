#!/bin/bash

sleep 30

celery --app=backend.tasks.celery_app:celery worker -l INFO -B
