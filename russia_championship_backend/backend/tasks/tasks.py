#celery -A backend.tasks.celery_app:celery worker --loglevel=INFO
import smtplib
from email.message import EmailMessage
from backend.tasks.celery_app import celery
from backend.config import settings

@celery.task
def send_new_password_on_email(email: str,
                               new_password: str):
    msg_content = new_password

    msg = EmailMessage()
    msg.set_content(f'Одноразовый код для доступа: {msg_content}', charset='utf-8')
    msg['Subject'] = 'Одноразовый код'
    msg['From'] = settings.SMTP_USER
    msg['To'] = email

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg)