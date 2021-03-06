# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-17 10:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coworks', '0022_cowork_price_per_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoworkRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0)),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('cowork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rating_cowork', to='coworks.Cowork')),
            ],
        ),
    ]
