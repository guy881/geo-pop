# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-06 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0003_auto_20180106_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
