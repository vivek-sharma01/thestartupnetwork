# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworks', '0013_auto_20180120_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactperson',
            name='alternate_no',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]