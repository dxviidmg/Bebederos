# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-19 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bebederos', '0067_sistemabebedero_packing_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sistemabebedero',
            name='no_serie_sp',
        ),
    ]
