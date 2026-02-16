from django.contrib import admin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'phone_number', 'is_subscriber']


admin.site.register(CustomUser, CustomUserAdmin)