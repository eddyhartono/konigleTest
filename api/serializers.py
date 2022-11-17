from django.forms import ValidationError
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers
from .models import emailList

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = emailList
        fields = "__all__"
        ordering = ['-date_action']

    def validate_email(self, value):
        try:
            check_email = emailList.objects.get(email__exact=value)
            if check_email :
                raise ValidationError('Email is already Signed Up')
        except ObjectDoesNotExist:
            return value