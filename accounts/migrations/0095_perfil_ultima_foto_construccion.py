# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-09 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0094_perfil_prioridad'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='ultima_foto_construccion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
