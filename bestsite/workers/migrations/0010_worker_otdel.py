# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-05 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otdels', '0001_initial'),
        ('workers', '0009_auto_20180705_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='otdel',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='otdels.Otdel'),
        ),
    ]
