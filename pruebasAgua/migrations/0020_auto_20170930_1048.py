# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-30 15:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruebasAgua', '0019_auto_20170930_1036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segundaprueba',
            old_name='sugerencias_sp',
            new_name='aprobacion_interna',
        ),
    ]
