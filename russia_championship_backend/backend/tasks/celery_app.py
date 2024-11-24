from celery import Celery
from celery.schedules import crontab
from backend.config import settings

celery = Celery(
    'tasks',
    broker=settings.RABBITMQ_URL,
    include=['backend.tasks.tasks'],
)

celery.conf.beat_schedule = {
    'Parse_pdf_from_website': {
        'task': 'parse_pdf_from_website',
        'schedule': crontab(minute='0', hour='7'), #по нулевому меридиану время
    },
    'Notificate_in_email': {
        'task': 'notificate_in_email',
        'schedule': crontab(minute='30', hour='15'), #по нулевому меридиану время
    },
    'Compare_json': {
        'task': 'compare_json',
        'schedule': crontab(minute='30', hour='16'), #по нулевому меридиану время
    },
    'Pdf_parse': {
        'task': 'pdf_parse',
        'schedule': crontab(minute='30', hour='8'), #по нулевому меридиану время
    },
     'Dump_in_db_scheduler': {
        'task': 'dump_in_db_scheduler',
        'schedule': crontab(minute='30', hour='9'), #по нулевому меридиану время
    },
}