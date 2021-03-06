# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-09 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0002_auto_20180606_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_contact', models.IntegerField(choices=[(0, 'phone'), (1, 'e-mail')])),
                ('contact', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'verbose_name': 'Работяга', 'verbose_name_plural': 'Рабочих'},
        ),
        migrations.AddField(
            model_name='contact',
            name='id_worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.Worker'),
        ),
    ]
