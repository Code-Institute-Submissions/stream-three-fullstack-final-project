# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-19 20:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cycles', '0010_auto_20180719_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='cycles',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_client', to=settings.AUTH_USER_MODEL),
        ),
    ]
