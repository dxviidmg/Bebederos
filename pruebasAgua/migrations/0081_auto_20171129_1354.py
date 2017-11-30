# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-29 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebasAgua', '0080_auto_20171127_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segundaprueba',
            name='aprobacion',
        ),
        migrations.AddField(
            model_name='segundaprueba',
            name='validacion',
            field=models.CharField(choices=[('Validado', 'Validado'), ('No validado', 'No validado')], default='En espera', max_length=11, verbose_name='Validación'),
        ),
    ]
