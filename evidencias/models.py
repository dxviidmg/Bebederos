from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from bebederos.models import SistemaBebedero

class Plantilla(models.Model):
	subido_por = models.ForeignKey(User)
	nombre = models.CharField(max_length=30)
	archivo = models.FileField(upload_to='plantillas/%Y/%m/%d/')
	creacion = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['nombre']

class Evidencia(models.Model):
	nombre_choices = (
		('Pre-instalación', (
			('Dictamen de ubicación', 'Dictamen de ubicación'),
			('Constancia de toma de agua municipal', 'Constancia de toma de agua municipal'),
			('Constancia de llegada de agua al laboratorio', 'Constancia de llegada de agua al laboratorio'),
			('Resultados del primer análisis de la calidad del agua', 'Resultados del primer análisis de la calidad del agua'),
			('Validación de la calidad del agua', 'Validación de la calidad del agua'),
		)
		),
		('Instalación', (
			('Constancia de llegada de material', 'Constancia de llegada de material'),
			)
		),
		('Post-Instalación', (
			('Constancia de la llegada de la segunda muestra de agua al laboratorio', 'Constancia de la llegada de la segunda muestra de agua al laboratorio'),
			('Resultados del segundo análisis de la calidad del agua', 'Resultados del segundo análisis de la calidad del agua'),
			('Resultados del segundo análisis de la calidad del agua', 'Resultados del segundo análisis de la calidad del agua'),
			('Dictamen del sistema avalado', 'Dictamen del sistema avalado'),
					('Recibo de entrega de llaves', 'Recibo de entrega de llaves'),
							('Acta de inicio de funcionamiento', 'Acta de inicio de funcionamiento'),

			)
		),
		('Revisiones', (
			('Revisión mensual (1er mes)', 'Revisión mensual (1er mes)'),
			('Revisión mensual (2do mes)', 'Revisión mensual (2do mes)'),
			('Revisión mensual (3er mes)', 'Revisión mensual (3er mes)'),
			('Revisión mensual (4to mes)', 'Revisión mensual (4to mes)'),
			('Revisión mensual (5to mes)', 'Revisión mensual (5to mes)'),
			('Constancia de lavado y desinfeccion de tinaco y cisterna (6to mes)', 'Constancia de lavado y desinfeccion de tinaco y cisterna (6to mes)'),
			('Revisión mensual (7mo mes)', 'Revisión mensual (7mo mes)'),
			('Constancia de prueba periodica (8mo mes)', 'Constancia de prueba periodica (8mo mes)'),
		)
		),
	)

	sistemabebedero = models.ForeignKey(SistemaBebedero)
	subido_por = models.ForeignKey(User)
	nombre = models.CharField(max_length=100, choices=nombre_choices)
	archivo = models.FileField(upload_to='expedientes/archivos/%Y/%m/%d/')
	foto = models.FileField(upload_to='expedientes/fotos/%Y/%m/%d/')
	video = models.FileField(upload_to='expedientes/videos/%Y/%m/%d/')
	creacion = models.DateTimeField(default=timezone.now)
	aprobado = models.BooleanField(default=False)

	def __str__(self):
		return '{} de {}'.format(self.nombre, self.sistemabebedero)

	class Meta:
		ordering = ['sistemabebedero', 'creacion']