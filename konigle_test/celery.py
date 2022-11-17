import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'konigle_test.settings')

app = Celery('konigle_test')
app.conf.enable_utc = False
# Change this timezone based on your location
app.conf.update(timezone = 'Asia/Jakarta')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# CELERY BEAT
# On the project settings, email backend is set to FILE BASED, to see the log of the email, please check on 'store_celery_emails_temp' folder
app.conf.beat_schedule = {
    'send_email_every_Monday_Wednesday' : {
        'task' : 'unity.tasks.send_email',
        'schedule' : crontab(day_of_week = '1,3')
        # 'schedule' : crontab(hour = '13', minute='10')
        }
    }

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')