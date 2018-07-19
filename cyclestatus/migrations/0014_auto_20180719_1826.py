# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-19 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cycleporthole', '0007_auto_20180715_1617'),
        ('cyclestatus', '0013_auto_20180719_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceAction',
            fields=[
                ('action', models.BooleanField(default=False)),
                ('invoice', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cycleporthole.Invoices')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='POAction',
            fields=[
                ('action', models.BooleanField(default=False)),
                ('po', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cycleporthole.PurchaseOrder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuoteAction',
            fields=[
                ('action', models.BooleanField(default=False)),
                ('quote', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cycleporthole.Quotes')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='invoicesstatus',
            name='action',
        ),
        migrations.RemoveField(
            model_name='postatus',
            name='action',
        ),
        migrations.RemoveField(
            model_name='quotestatus',
            name='action',
        ),
    ]
