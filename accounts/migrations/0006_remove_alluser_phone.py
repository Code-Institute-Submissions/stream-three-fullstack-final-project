# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-10 20:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180710_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alluser',
            name='phone',
        ),
    ]