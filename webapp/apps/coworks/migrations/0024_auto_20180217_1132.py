# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-17 11:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworks', '0023_coworkrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coworkrating',
            name='id',
        ),
        migrations.AlterField(
            model_name='coworkrating',
            name='user_id',
            field=models.CharField(default=datetime.datetime(2018, 2, 17, 11, 32, 47, 936806), max_length=100, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
