from django.contrib import admin
from .models import User_Account, Transaction_history

@admin.register(User_Account)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'balance')

@admin.register(Transaction_history)
class Transaction_historyAdmin(admin.ModelAdmin):
    list_display =('user_id', 'order_id',  'billing_name', 'date', 'amount',  'status',  'payment_method', )