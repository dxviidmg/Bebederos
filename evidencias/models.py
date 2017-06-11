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
			('Convenio de ubicación', 'Convenio de ubicación'),
			('Primer análisis de la calidad del agua', 'Primer análisis de la calidad del agua'),
		)
		),
		('Instalación', (
			('Llegada de material', 'Llegada de material'),
			)
		),
		('Revisiones', (
			('Primera revisión mensual', 'Primera revisión mensual'),
			('Segunda revisión mensual', 'Segunda revisión mensual'),
			('Tercera revisión mensual', 'Tercera revisión mensual'),
			('Cuarta revisión mensual', 'Cuarta revisión mensual'),
			('Quinta revisión mensual', 'Quinta revisión mensual'),
			('Sexta revisión mensual', 'Sexta revisión mensual'),
		)
		),
	)

	sistemabebedero = models.ForeignKey(SistemaBebedero)
	subido_por = models.ForeignKey(User)
	nombre = models.CharField(max_length=50, choices=nombre_choices)
	archivo = models.FileField(upload_to='expedientes/archivos/%Y/%m/%d/')
	foto = models.FileField(upload_to='expedientes/fotos/%Y/%m/%d/')
	video = models.FileField(upload_to='expedientes/videos/%Y/%m/%d/')
	creacion = models.DateTimeField(default=timezone.now)
	aprobado = models.BooleanField(default=False)

	def __str__(self):
		return '{} de {}'.format(self.nombre, self.sistemabebedero)

	class Meta:
		ordering = ['nombre']