import datetime

from celery import shared_task
from users.models import User
from users.services import send_birthday_email


@shared_task
def check_birthday():
    users = User.objects.all()
    current_date = datetime.date.today()
    for user in users:
        if user.birth_date is not None:
            if user.birth_date.month == current_date.month and user.birth_date.day == current_date.day:
                send_birthday_email(user)
