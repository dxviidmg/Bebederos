# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-08 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0075_auto_20171107_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='telefono',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Teléfono'),
        ),
    ]
