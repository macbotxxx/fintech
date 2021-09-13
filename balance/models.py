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



