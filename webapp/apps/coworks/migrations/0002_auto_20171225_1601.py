# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coworks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cowork',
            old_name='contact_perspn',
            new_name='contact_person',
        ),
    ]
