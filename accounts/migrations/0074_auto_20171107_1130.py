# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-07 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0073_perfil_mantenimientos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='mantenimientos',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
