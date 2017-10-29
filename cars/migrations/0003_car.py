# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0002_delete_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avail', models.BooleanField()),
                ('state', models.TextField(max_length=50)),
                ('car_id', models.IntegerField()),
                ('coord', models.TextField(max_length=100)),
                ('velo', models.IntegerField()),
            ],
        ),
    ]