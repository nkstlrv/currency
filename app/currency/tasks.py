from celery import shared_task
import time
from django.core.mail import send_mail


@shared_task
def demo_task():
    for i in range(10):
        print("TESTING WORKER")
        time.sleep(0.1)


@shared_task
def send_contactus_email(cleaned_data: dict):
    email_body = f"""
            From: {cleaned_data['email_from']}
            Subject: {cleaned_data['subject']}
            Message: {cleaned_data['message']}
            """

    from django.conf import settings

    send_mail(
        "Contact Us",
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )
    return True
