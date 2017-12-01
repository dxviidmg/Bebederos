# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-01 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas', '0046_auto_20171120_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitadeacuerdo',
            name='acta_acuerdos',
            field=models.FileField(blank=True, null=True, upload_to='visitas/actas/%Y/%m/%d/', verbose_name='Acta de acuerdos'),
        ),
        migrations.AlterField(
            model_name='visitadeacuerdo',
            name='cedula_identificacion',
            field=models.FileField(blank=True, null=True, upload_to='visita/identificaciones/%Y/%m/%d/', verbose_name='Cédula de identificación básica'),
        ),
    ]
