# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworks', '0004_auto_20171226_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactperson',
            name='alternate_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='cowork',
            name='landmark',
            field=models.TextField(blank=True, null=True),
        ),
    ]