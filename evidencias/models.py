from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from bebederos.models import SistemaBebedero

class Plantilla(models.Model):
	subido_por = models.ForeignKey(User)
	nombre = models.CharField(max_length=30)
	archivo = models.FileField(upload_to='plantillas/%Y/%m/%d/')
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['nombre']

class EvidenciaPrevia(models.Model):
	nombre_choices = (

		('Acta de acuerdos y dictamen de ubicación', 'Acta de acuerdos y dictamen de ubicación'),
		('Constancia de visita', 'Constancia de visita'),
		('Constancia de primera toma de agua', 'Constancia de primera toma de agua'),
		('Constancia de llegada de agua al laboratorio', 'Constancia de llegada de agua al laboratorio'),
		('Resultados del primer análisis de la calidad del agua', 'Resultados del primer análisis de la calidad del agua'),
		('Validación de la calidad del agua', 'Validación de la calidad del agua'),
		('Carta de presentación', 'Carta de presentación'),

	)

	aprobacion_imta_choices = (
		('Aprobado', 'Aprobado'),
		('No aprobado', 'No aprobado'),
	)

	sistemabebedero = models.ForeignKey(SistemaBebedero)
	subido_por = models.ForeignKey(User)
	nombre = models.CharField(max_length=100, choices=nombre_choices)
	archivo = models.FileField(upload_to='expedientes/archivos/%Y/%m/%d/', verbose_name="Documento (solo pdf)")
	foto = models.FileField(upload_to='expedientes/fotos/%Y/%m/%d/', verbose_name="Fotografía (Con camara de 5 megapixeles en adelante)")
	video = models.FileField(upload_to='expedientes/videos/%Y/%m/%d/', verbose_name="Video (Con camara de 5 megapixeles en adelante)")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de registro")
	aprobado = models.BooleanField(default=False)
	aprobacion_imta = models.CharField(choices=aprobacion_imta_choices, max_length=20, null=True, blank=True)

	def __str__(self):
		return '{} de {}'.format(self.nombre, self.sistemabebedero)

	class Meta:
		ordering = ['sistemabebedero', 'creacion']

class EvidenciaInstalacion(models.Model):
	nombre_choices = (
		('Constancia de llegada de material', 'Constancia de llegada de material'),
		('Acta de inicio de trabajos', 'Acta de inicio de trabajos'),
		('Constancia de realización de la fase: Trabajos preliminares', 'Constancia de realización de la fase: Trabajos preliminares'),
		('Constancia de realización de la fase: Albañileria', 'Constancia de realización de la fase: Albañileria'),
		('Constancia de realización de la fase: Herreria', 'Constancia de realización de la fase: Herreria'),
		('Constancia de realización de la fase: Instalaciones', 'Constancia de realización de la fase: Instalaciones'),
		('Constancia de realización de la fase: Bebedero', 'Constancia de realización de la fase: Bebedero'),
	)

	sistemabebedero = models.ForeignKey(SistemaBebedero)
	subido_por = models.ForeignKey(User)
	nombre = models.CharField(max_length=100, choices=nombre_choices)
	archivo = models.FileField(upload_to='expedientes/archivos/%Y/%m/%d/', verbose_name="Documento (solo pdf)")
	foto = models.FileField(upload_to='expedientes/fotos/%Y/%m/%d/', verbose_name="Fotografía (Con camara de 5 megapixeles en adelante)")
	video = models.FileField(upload_to='expedientes/videos/%Y/%m/%d/', verbose_name="Video (Con camara de 5 megapixeles en adelante)")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de registro")
	aprobado = models.BooleanField(default=False)

	def __str__(self):
		return '{} de {}'.format(self.nombre, self.sistemabebedero)

	class Meta:
		ordering = ['sistemabebedero', 'creacion']

class EvidenciaPostInstalacion(models.Model):
	nombre_choices = (
		('Constancia de segunda toma de agua', 'Constancia de segunda toma de agua'),
		('Constancia de llegada de agua al laboratorio', 'Constancia de llegada de agua al laboratorio'),
		('Resultados del segundo análisis de la calidad del agua', 'Resultados del segundo análisis de la calidad del agua'),
		('Dictamen de sistema bebedero avalado', 'Dictamen de sistema bebedero avalado'),
		('Acta de inicio de funcionamiento', 'Acta de inicio de funcionamiento'),
	)

	sistemabebedero = models.ForeignKey(SistemaBebedero)
	subido_por = models.ForeignKey(User)
	nombre = models.CharField(max_length=100, choices=nombre_choices)
	archivo = models.FileField(upload_to='expedientes/archivos/%Y/%m/%d/', verbose_name="Documento (solo pdf)")
	foto = models.FileField(upload_to='expedientes/fotos/%Y/%m/%d/', verbose_name="Fotografía (Con camara de 5 megapixeles en adelante)")
	video = models.FileField(upload_to='expedientes/videos/%Y/%m/%d/', verbose_name="Video (Con camara de 5 megapixeles en adelante)")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de registro")
	aprobado = models.BooleanField(default=False)

	def __str__(self):
		return '{} de {}'.format(self.nombre, self.sistemabebedero)

	class Meta:
		ordering = ['sistemabebedero', 'creacion']