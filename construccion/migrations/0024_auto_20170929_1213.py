# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-29 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construccion', '0023_remove_evidenciaconstruccion_aprobacion_residente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terminodetrabajo',
            name='plantilla_fotografica',
        ),
        migrations.RemoveField(
            model_name='terminodetrabajo',
            name='reporte_segunda_toma',
        ),
        migrations.AddField(
            model_name='terminodetrabajo',
            name='acta_termino',
            field=models.FileField(default='default.pdf', upload_to='trabajos/inicio/acta/%Y/%m/%d/', verbose_name='Acta de termino de trabajo'),
        ),
        migrations.AddField(
            model_name='terminodetrabajo',
            name='video',
            field=models.FileField(default='default.pdf', upload_to='instalaciones/plantilla/%Y/%m/%d/', verbose_name='Evidencia audiovisual'),
        ),
        migrations.AlterField(
            model_name='instalacionbebedero',
            name='memoria_calculo',
            field=models.FileField(upload_to='instalaciones/memorias/%Y/%m/%d/', verbose_name='Memorias de cálculo'),
        ),
    ]
