# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0003_auto_20171112_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='permissions_level',
            field=models.CharField(choices=[('AM', 'Prawo jazdy kategori AM'), ('A', 'Prawo jazdy kategori A'), ('A1', 'Prawo jazdy kategori A1'), ('A2', 'Prawo jazdy kategori A2'), ('B', 'Prawo jazdy kategori B'), ('B+E', 'Prawo jazdy kategori B+E'), ('C', 'Prawo jazdy kategori C'), ('C+E', 'Prawo jazdy kategori C+E'), ('C1', 'Prawo jazdy kategori C1'), ('C1+E', 'Prawo jazdy kategori C+E'), ('D', 'Prawo jazdy kategori D'), ('D+E', 'Prawo jazdy kategori D+E'), ('D1', 'Prawo jazdy kategori D1'), ('D1+E', 'Prawo jazdy kategori D1+E')], max_length=50),
        ),
    ]
