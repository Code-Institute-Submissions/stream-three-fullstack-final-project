# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-31 20:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('managejobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 31, 20, 52, 44, 455723, tzinfo=utc)),
        ),
    ]