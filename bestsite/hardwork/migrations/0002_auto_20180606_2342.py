# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-06 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardwork', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='worker',
            name='status',
            field=models.IntegerField(choices=[(0, 'new'), (1, 'work'), (2, 'deleled')]),
        ),
    ]
