# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-12 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebasAgua', '0084_auto_20171206_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segundaprueba',
            name='foto_toma_agua_1',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/1/fotos/%Y/%m/%d/', verbose_name='Fotografía de fachada de la escuela donde se muestre el CTT'),
        ),
        migrations.AlterField(
            model_name='segundaprueba',
            name='foto_toma_agua_2',
            field=models.FileField(blank=True, null=True, upload_to='pruebas/1/fotos/%Y/%m/%d/', verbose_name='Fotografía de muestra en el punto de muestro'),
        ),
    ]
