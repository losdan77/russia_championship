#!/bin/bash

sleep 20

celery --app=backend.tasks.celery_app:celery worker -l INFO -B
