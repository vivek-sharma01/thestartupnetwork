# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-11 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworks', '0021_auto_20180201_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='cowork',
            name='price_per_week',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
