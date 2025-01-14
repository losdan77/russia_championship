#!/bin/bash

sleep 35

celery --app=backend.tasks.celery_app:celery worker -l INFO

