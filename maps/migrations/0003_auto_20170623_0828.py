# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_auto_20170622_2218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='map',
            options={'ordering': ['name'], 'verbose_name': 'карта', 'verbose_name_plural': 'карты'},
        ),
        migrations.AddField(
            model_name='map',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
