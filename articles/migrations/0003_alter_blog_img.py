# Generated by Django 3.2.6 on 2021-08-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210827_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(help_text='Blog post image ', null=True, unique=True, upload_to='blog_post/', verbose_name='Post Image'),
        ),
    ]
