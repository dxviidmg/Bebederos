from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class PrimerPrueba(models.Model):
	aprobacion_choices = (
		("En espera", "En espera"),
		("Aprobado", "Aprobado"),
		("No aprobado", "No aprobado"),
	)
	escuela = models.OneToOneField(User)
	constancia_recepcion = models.FileField(upload_to='pruebas/1/constancia/%Y/%m/%d/', verbose_name="Constancia de recepción de muestra de laboratorio")
	video = models.FileField(upload_to='pruebas/1/video/%Y/%m/%d/', verbose_name="Video")
	resultados = models.FileField(upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name="Resultados")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	laboratorio = models.ForeignKey(User, related_name="lab_primer_prueba")
	aprobacion = models.CharField(max_length=11, default="En espera", choices=aprobacion_choices)

	def __str__(self):
		return '{} para escuela'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Primeras pruebas'

class SegundaPrueba(models.Model):
	aprobacion_choices = (
		("En espera", "En espera"),
		("Aprobado", "Aprobado"),
		("No aprobado", "No aprobado"),
	)
	escuela = models.OneToOneField(User)
	constancia_recepcion = models.FileField(upload_to='pruebas/1/constancia/%Y/%m/%d/', verbose_name="Constancia de recepción de muestra de laboratorio")
	video = models.FileField(upload_to='pruebas/1/video/%Y/%m/%d/', verbose_name="Video")
	resultados = models.FileField(upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name="Resultados")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	laboratorio = models.ForeignKey(User, related_name="lab_segunda_prueba")
	aprobacion = models.CharField(max_length=11, default="En espera", choices=aprobacion_choices)
	def __str__(self):
		return '{} para escuela'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Segundas pruebas'