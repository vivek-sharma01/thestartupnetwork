# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-14 11:37
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworks', '0010_cowork_no_of_workstattion'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershipbenefits',
            name='suitable_for',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
    ]