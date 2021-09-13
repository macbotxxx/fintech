# Generated by Django 3.2.6 on 2021-09-06 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0, help_text='The user balance for this account', null=True, verbose_name='User Balance')),
                ('user_id', models.ForeignKey(help_text='The user that this account balance belong to', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ID')),
            ],
            options={
                'verbose_name': 'USer Account Balance',
                'verbose_name_plural': 'USer Accounts Balance',
            },
        ),
    ]
