# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-17 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evidencias', '0010_auto_20170715_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidencia',
            name='archivo',
            field=models.FileField(upload_to='expedientes/archivos/%Y/%m/%d/', verbose_name='Documento (solo pdf)'),
        ),
    ]
