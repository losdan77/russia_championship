#!/bin/bash

sleep 10

celery --app=backend.tasks.celery_app:celery worker -l INFO

