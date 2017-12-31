# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coworks', '0002_auto_20171225_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cowork',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_coworks', to='coworks.Location'),
        ),
    ]
