# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_auto_20170717_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='business_name',
            field=models.CharField(blank=True, max_length=60, verbose_name='Business Registered Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='business_reg_no',
            field=models.CharField(blank=True, max_length=10, verbose_name='Business Registration Number'),
        ),
    ]
