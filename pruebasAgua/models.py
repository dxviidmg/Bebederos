from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class PrimerPrueba(models.Model):
	escuela = models.OneToOneField(User)
	constancia_de_recepcion = models.FileField(upload_to='pruebas/1/constancia/%Y/%m/%d/', verbose_name="Constancia de recepción de muestra de laboratorio")
	video = models.FileField(upload_to='pruebas/1/video/%Y/%m/%d/', verbose_name="Video")
	resultados = models.FileField(upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name="Resultados")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	laboratorio = models.ForeignKey(User, related_name="lab_primer_prueba")

	def __str__(self):
		return '{} para escuela'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Primeras pruebas'

class SegundaPrueba(models.Model):
	escuela = models.OneToOneField(User)
	constancia_de_recepcion = models.FileField(upload_to='pruebas/1/constancia/%Y/%m/%d/', verbose_name="Constancia de recepción de muestra de laboratorio")
	video = models.FileField(upload_to='pruebas/1/video/%Y/%m/%d/', verbose_name="Video")
	resultados = models.FileField(upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name="Resultados")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	laboratorio = models.ForeignKey(User, related_name="lab_segunda_prueba")

	def __str__(self):
		return '{} para escuela'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Segundas pruebas'