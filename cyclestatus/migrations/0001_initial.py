# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-20 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cycleporthole', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoicesStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approve', models.BooleanField(default=False)),
                ('contest', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, max_length=150)),
                ('invoice', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cycleporthole.Invoices')),
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
                ('comment', models.TextField(blank=True, max_length=150)),
                ('po', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cycleporthole.PurchaseOrder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuoteStatus',
            fields=[
                ('approve', models.BooleanField(default=False)),
                ('contest', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, max_length=150)),
                ('quote', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cycleporthole.Quotes')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
