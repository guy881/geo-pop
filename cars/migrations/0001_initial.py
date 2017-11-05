# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0003_driver_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField()),
                ('state', models.TextField(max_length=50)),
                ('coordinates', models.TextField(max_length=100)),
                ('velocity', models.IntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver')),
            ],
        ),
    ]
