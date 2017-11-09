# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_remove_car_car_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='last_location',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='regions.GeoLocalization'),
        ),
    ]
