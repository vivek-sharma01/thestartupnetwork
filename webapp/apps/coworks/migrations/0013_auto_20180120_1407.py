# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coworks', '0012_cowork_banner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cowork',
            name='amenity',
            field=models.ManyToManyField(blank=True, null=True, related_name='cowork_amenities', to='coworks.Amenity'),
        ),
        migrations.AlterField(
            model_name='cowork',
            name='contact_person',
            field=models.ManyToManyField(blank=True, null=True, related_name='cowork_contactperson', to='coworks.ContactPerson'),
        ),
        migrations.AlterField(
            model_name='cowork',
            name='neighbour_amenity',
            field=models.ManyToManyField(blank=True, null=True, related_name='cowork_neighbouramenities', to='coworks.NeighbourAmenity'),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='cowork',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cowork_price', to='coworks.Cowork'),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='membership',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='membership_price', to='coworks.MembershipBenefits'),
        ),
    ]