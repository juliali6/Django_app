from time import sleep
from celery import shared_task


@shared_task
def email_reg_task():
    """Send email with o'clock"""

    sleep(5)
    return None