# Generated by Django 3.2.6 on 2022-01-25 15:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_tasks_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='users',
            field=models.ManyToManyField(related_name='Task', to=settings.AUTH_USER_MODEL),
        ),
    ]
