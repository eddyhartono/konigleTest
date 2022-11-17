from datetime import date
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

from celery import shared_task
from api.models import emailList

@shared_task(bind=True)
def send_email(self):
    this_month = date.today().month
    total_subs_this_month = emailList.objects.filter(subscribe = True, date_action__month = this_month).count()
    seller = get_user_model().objects.get(id=1)
    
    email_subject = 'Hi ' + seller.first_name + ' ' + seller.last_name + ', Your Unity Statistic Report is ready'
    email_body = 'Hi ' + seller.first_name + ' ' + seller.last_name + ',\nYou have ' + str(total_subs_this_month) + ' new email(s) subscriber this month\n\n\n\n\nRegards,\nUnity Team'
    send_to = seller.email
    send_mail(
        subject = email_subject,
        message = email_body,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = [send_to],
        fail_silently = True,
        )
    return 'Sent'