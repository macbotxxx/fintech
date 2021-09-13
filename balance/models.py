from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class User_Account (models.Model):
    """
    Creating an account for the registered user
    """
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name=_('User ID'),
        null=True,
        help_text=_('The user that this account balance belong to')
        )

    balance = models.FloatField (
        verbose_name=_('User Balance'),
        default=0,
        null=True,
        help_text=_('The user balance for this account')
    )

    class Meta:
        verbose_name = _('USer Account Balance')
        verbose_name_plural = _('USer Accounts Balance')

    def __str__(self):
        return self.user_id

@receiver(post_save, sender = User)
def create_user_balance(sender ,instance, created, **kwargs):
    if created:
        User_Account.objects.create(user_id = instance)


class Transaction_history(models.Model):
    user_id = models.ForeignKey(
        User,on_delete=models.CASCADE,
        verbose_name=_('User'),
        null=True,
        help_text=_('The user')
        )

    order_id = models.CharField(
        verbose_name=_('User Order ID'),
        max_length=500, null=True,
        help_text=_('the user order id')
        )

    billing_name = models.CharField(
        verbose_name=_('Billing Name'),
        max_length = 500, null=True,
        help_text=_('the billing name')
        )
    
    date = models.DateTimeField(
        verbose_name=_('Transaction Date'),
        auto_now_add=True,
        null=True,
        help_text=_('The transaction date time ')
    )

    amount = models.FloatField(
        verbose_name=_('Amount Been Paid'),
        null=True,
        help_text=_('The total amount been paid by the user')
    )

    status = models.CharField(
        verbose_name=_('Status'),
        max_length = 500,
        null=True,
        help_text=_('The status of the transaction')
    )

    payment_method = models.CharField(
        verbose_name=_('Payment Method'),
        max_length = 500,
        default = 'Online Payment',
        null = True, 
        help_text=_('The payment method for the order')
    )

    def __str__(self):
        return str(self.user_id) 


    class Meta:
        verbose_name = _('All Transactions')
        verbose_name_plural = _('All Transactions')

    
