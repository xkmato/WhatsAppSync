# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sync', '0003_auto_20170404_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
