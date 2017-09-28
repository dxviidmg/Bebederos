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

	#Fase de Toma de Agua / SI
	reporte_toma_agua = models.FileField(upload_to='pruebas/1/reporte_de_toma/%Y/%m/%d/', verbose_name="Reporte de toma de muestra", null=True, blank=True)
	video = models.FileField(upload_to='pruebas/1/video/%Y/%m/%d/', verbose_name="Video de toma de agua")

	#Fase de analisis / LAB
	resultados_laboratorio = models.FileField(upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name="Resultados de analísis de laboratorio", null=True, blank=True)

	#Fase de Sugerencias / ECA(Pilar)
	resultados_inifed = models.FileField(upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name="Resultados de analísis para INIFED", null=True, blank=True)
	sugerencias_sp = models.FileField(upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name="Sugerencia de Sistema Potabilizador", null=True, blank=True)

	#Fase de confirmación de INIFED
	dictamen_sistema_potabilizador = models.FileField(upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name="Dictamen del sistema potabilizador a utilizar", null=True, blank=True)
	aprobacion = models.CharField(max_length=11, default="En espera", choices=aprobacion_choices, verbose_name="Aprobación")

	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	laboratorio = models.ForeignKey(User, related_name="lab_primer_prueba")


	def __str__(self):
		return '{}'.format(self.escuela)

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
	acta_segunda_prueba = models.FileField(upload_to='pruebas/2/acta_de_segunda_prueba/%Y/%m/%d/', verbose_name="Acta de segunda prueba", null=True, blank=True)
	reporte_toma_agua = models.FileField(upload_to='pruebas/2/reporte_de_toma/%Y/%m/%d/', verbose_name="Reporte de toma de muestra", null=True, blank=True)
	dictamen_validacion = models.FileField(upload_to='pruebas/2/validacion/%Y/%m/%d/', verbose_name="Dictamen de validación", null=True, blank=True)
	constancia_recepcion = models.FileField(upload_to='pruebas/2/constancia/%Y/%m/%d/', verbose_name="Constancia de recepción de muestra de laboratorio")
	video = models.FileField(upload_to='pruebas/2/video/%Y/%m/%d/', verbose_name="Video")
	resultados = models.FileField(upload_to='pruebas/2/resultados/%Y/%m/%d/', verbose_name="Resultados de muestreo")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	laboratorio = models.ForeignKey(User, related_name="lab_segunda_prueba")
	aprobacion = models.CharField(max_length=11, default="En espera", choices=aprobacion_choices, verbose_name="Aprobación")
	
	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Segundas pruebas'