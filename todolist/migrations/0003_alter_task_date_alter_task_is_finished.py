# Generated by Django 4.1 on 2022-09-28 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_task_is_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_finished',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]