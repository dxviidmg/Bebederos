# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-16 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0090_perfil_evidencias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Año',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.IntegerField()),
            ],
        ),
    ]
