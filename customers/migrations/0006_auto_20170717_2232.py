# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 14:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20170717_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_created_by_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_owned_by_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lead_owned_by_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
