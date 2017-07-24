# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 14:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bebederos', '0009_sistemabebedero_identificador'),
        ('evidencias', '0014_auto_20170717_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvidenciaInstalacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('Constancia de llegada de naterial', 'Constancia de llegada de naterial'), ('Constancia de realización de la fase: Trabajos preliminares', 'Constancia de realización de la fase: Trabajos preliminares'), ('Constancia de realización de la fase: Albañileria', 'Constancia de realización de la fase: Albañileria'), ('Constancia de realización de la fase: Herreria', 'Constancia de realización de la fase: Herreria'), ('Constancia de realización de la fase: Instalaciones', 'Constancia de realización de la fase: Instalaciones')], max_length=100)),
                ('archivo', models.FileField(upload_to='expedientes/archivos/%Y/%m/%d/', verbose_name='Documento (solo pdf)')),
                ('foto', models.FileField(upload_to='expedientes/fotos/%Y/%m/%d/', verbose_name='Fotografía (Con camara de 5 megapixeles en adelante)')),
                ('video', models.FileField(upload_to='expedientes/videos/%Y/%m/%d/', verbose_name='Video (Con camara de 5 megapixeles en adelante)')),
                ('creacion', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de registro')),
                ('aprobado', models.BooleanField(default=False)),
                ('sistemabebedero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bebederos.SistemaBebedero')),
                ('subido_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['sistemabebedero', 'creacion'],
            },
        ),
    ]
