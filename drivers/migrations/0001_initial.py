# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_id', models.IntegerField()),
                ('full_name', models.TextField(max_length=50)),
                ('gender', models.TextField(max_length=50)),
                ('pesel', models.TextField(max_length=11)),
                ('permissions_level', models.IntegerField()),
                ('phone_number', models.TextField(max_length=15)),
            ],
        ),
    ]