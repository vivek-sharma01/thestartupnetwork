# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworks', '0006_auto_20180113_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='seats',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
