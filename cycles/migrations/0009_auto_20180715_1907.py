# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-15 19:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycles', '0008_auto_20180715_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cycles',
            name='job_end',
        ),
        migrations.RemoveField(
            model_name='cycles',
            name='job_start',
        ),
    ]
