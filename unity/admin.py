from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',)

    fieldsets = [
        ("SELLER", {'fields': ['email','first_name', 'last_name','date_joined', 'is_staff']}),
    ]

admin.site.register(CustomUser, CustomUserAdmin)