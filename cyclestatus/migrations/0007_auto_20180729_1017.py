# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-29 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyclestatus', '0006_auto_20180729_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cyclestatus',
            name='approve_invoice',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cyclestatus',
            name='approve_po',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cyclestatus',
            name='approve_quote',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cyclestatus',
            name='cancelled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cyclestatus',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cyclestatus',
            name='contest_invoice',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cyclestatus',
            name='contest_po',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cyclestatus',
            name='contest_quote',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cyclestatus',
            name='pending',
            field=models.BooleanField(default=False),
        ),
    ]
