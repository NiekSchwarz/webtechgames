# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 16:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 16, 16, 26, 19, 611726)),
        ),
        migrations.AlterField(
            model_name='highscore',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 16, 16, 26, 19, 611726)),
        ),
    ]
