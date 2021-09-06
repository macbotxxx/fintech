from django.contrib import admin
from .models import User_Account

@admin.register(User_Account)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'balance')