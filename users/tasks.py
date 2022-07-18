from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_on_register():
    send_mail(
        'Welcome to Spoitify Clone',
        'Hey!,  Congratulations you have successfully registered to our platform.',
        'saad.ali@cogentlabs.co',
        ['saadali.sheikh7865@gmail.com'],
        fail_silently=False,
    )

