# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.CharField(max_length=254),
        ),
    ]
