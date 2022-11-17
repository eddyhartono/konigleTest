import datetime
from django.db import models

from humanfriendly import format_timespan

class emailList(models.Model):
    email = models.EmailField(verbose_name = "Buyer's email")
    subscribe = models.BooleanField(verbose_name = "Subscribe", default=True)
    date_action = models.DateTimeField(verbose_name = "Subscribed Date", auto_now=True)

    @property
    def duration_subs(self):
        now = datetime.datetime.utcnow()
        duration = now - self.date_action.replace(tzinfo=None)
        return format_timespan(duration,detailed=False,max_units=1)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Email List"
