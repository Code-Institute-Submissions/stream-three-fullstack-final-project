# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-11 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycles', '0005_auto_20180711_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cycles',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]