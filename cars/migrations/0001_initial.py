# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 00:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.IntegerField()),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=100)),
                ('production_year', models.IntegerField()),
                ('engine_volume', models.DecimalField(decimal_places=3, max_digits=8)),
                ('body_type', models.CharField(choices=[(1, 'Sedan'), (2, 'Hatchback'), (3, 'Kombi'), (4, 'SUV'), (5, 'Truck'), (6, 'Van')], default='1', max_length=10)),
                ('need_repair', models.TextField(max_length=50)),
                ('insurance_number', models.CharField(max_length=50)),
                ('is_available', models.BooleanField()),
                ('last_location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='regions.GeoLocalization')),
            ],
        ),
    ]
