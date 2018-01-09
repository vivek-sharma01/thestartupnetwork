# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworks', '0003_auto_20171226_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cowork',
            name='amenity',
            field=models.ManyToManyField(blank=True, related_name='cowork_amenities', to='coworks.Amenity'),
        ),
        migrations.AlterField(
            model_name='cowork',
            name='contact_person',
            field=models.ManyToManyField(blank=True, related_name='cowork_contactperson', to='coworks.ContactPerson'),
        ),
        migrations.AlterField(
            model_name='cowork',
            name='neighbour_amenity',
            field=models.ManyToManyField(blank=True, related_name='cowork_neighbouramenities', to='coworks.NeighbourAmenity'),
        ),
    ]