# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-11 16:45
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180204_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]