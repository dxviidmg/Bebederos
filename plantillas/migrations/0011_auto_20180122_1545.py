# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-22 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantillas', '0010_auto_20171201_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantilla',
            name='fase',
            field=models.CharField(choices=[('1', 'Todas'), ('2', 'Pruebas de calidad de agua'), ('3', 'Visita de acuerdos'), ('4', 'Inicio de trabajo'), ('5', 'Construcción e instalación de Sistema bebedero'), ('6', 'Inicio de funcionamiento'), ('7', 'Mantenimiento')], max_length=100),
        ),
    ]
