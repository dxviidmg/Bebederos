# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-18 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0062_zona_superintendente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='tipo',
            field=models.CharField(choices=[('Administrador', 'Administrador'), ('CEO', 'CEO'), ('SI', 'Superintendente'), ('Ejecutora', 'Ejecutora'), ('Escuela', 'Escuela'), ('Laboratorio', 'Laboratorio'), ('INIFED', 'INIFED'), ('CEstatal', 'Coordinador Estatal de INIFED'), ('RTINIFED', 'Residente Técnico de INIFED'), ('IMTA', 'IMTA'), ('PQ', 'Procesos Químicos (Calidad de Agua)'), ('PM', 'Planta y Manufactura')], max_length=30),
        ),
    ]
