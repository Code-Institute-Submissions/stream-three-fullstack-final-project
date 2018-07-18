# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-18 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cycleporthole', '0007_auto_20180715_1617'),
        ('cyclestatus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoicesStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approve', models.BooleanField(default=False)),
                ('contest', models.BooleanField(default=False)),
                ('urgent', models.BooleanField(default=False)),
                ('comment', models.BooleanField(default=False)),
                ('invoices', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cycleporthole.Invoices')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='POStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approve', models.BooleanField(default=False)),
                ('contest', models.BooleanField(default=False)),
                ('urgent', models.BooleanField(default=False)),
                ('comment', models.BooleanField(default=False)),
                ('po', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cycleporthole.PurchaseOrder')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
