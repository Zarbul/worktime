# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-09 20:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0004_auto_20180609_2325'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adres',
            new_name='Adress',
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'verbose_name_plural': 'Рабочие'},
        ),
    ]