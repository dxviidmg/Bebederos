# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-27 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bebederos', '0023_auto_20170927_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sistemabebedero',
            name='identificador_mb',
            field=models.CharField(default='1', max_length=20, verbose_name='Identificador de mueble bebedero'),
        ),
        migrations.AlterField(
            model_name='sistemabebedero',
            name='sistema_de_potabilizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sistema_potabilizacion', to='bebederos.SistemaPotabilizacion'),
        ),
    ]
