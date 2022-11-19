from rest_framework import serializers
from .models import emailList

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = emailList
        fields = "__all__"
        ordering = ['-date_action']
