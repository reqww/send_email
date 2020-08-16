from send_email.celery import app as celery_app

from .service import send

@celery_app.task
def send_spam_email(user_email):
    print('Я тут')
    # send(user_email)