# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-26 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworks', '0017_amenity_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.CharField(blank=True, default='India', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]