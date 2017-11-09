# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0001_initial'),
        ('cars', '0003_car_body_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='last_location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='regions.GeoLocalization'),
        ),
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(choices=[('sedan', 'Sedan'), ('hatchback', 'Hatchback'), ('kombi', 'Kombi'), ('suv', 'SUV'), ('truck', 'Truck'), ('van', 'Van')], default='1', max_length=10),
        ),
    ]