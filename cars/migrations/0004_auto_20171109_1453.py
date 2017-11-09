# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20171109_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(choices=[('1', 'Sedan'), ('2', 'Hatchback'), ('3', 'Kombi'), ('4', 'SUV'), ('5', 'Truck'), ('6', 'Van')], default='1', max_length=10),
        ),
    ]