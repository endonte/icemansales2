# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=200, verbose_name='Category'),
        ),
    ]