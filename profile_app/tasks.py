from time import sleep
from celery import shared_task


@shared_task
def email_reg_task():
    sleep(5)
    return None