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
	reporte_toma_agua = models.FileField(upload_to='pruebas/1/reporte_de_toma/%Y/%m/%d/', verbose_name="Reporte de toma de muestra")
	foto_toma_agua = models.FileField(upload_to='pruebas/1/fotos/%Y/%m/%d/', verbose_name="Evidencia fotográfica de toma de agua")

	#Fase de analisis / LAB
	resultados_laboratorio = models.FileField(upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name="Resultados de análisis de laboratorio", null=True, blank=True)
	foto_recepcion = models.FileField(upload_to='pruebas/1/fotos/%Y/%m/%d/', verbose_name="Evidencia fotográfica de recepción de muestra", null=True, blank=True)

	#Fase de Sugerencias / ECA(Pilar)
	resultados_IMTA = models.FileField(upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name="Resultados de análisis con propuesta de sistema potabilizador para visto bueno de IMTA", null=True, blank=True)

	#Fase de confirmación de IMTA
	dictamen_sistema_potabilizador = models.FileField(upload_to='pruebas/1/dictamen/%Y/%m/%d/', verbose_name="Dictamen del sistema potabilizador a utilizar", null=True, blank=True)
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

	#Fase de Toma de Agua / SI
	reporte_toma_agua = models.FileField(upload_to='pruebas/2/reporte_de_toma/%Y/%m/%d/', verbose_name="Reporte de toma de muestra")
	foto_toma_agua = models.FileField(upload_to='pruebas/2/video/%Y/%m/%d/', verbose_name="Evidencia fotográfica de toma de agua")

	#Fase de analisis / LAB
	resultados_laboratorio = models.FileField(upload_to='pruebas/2/resultados/%Y/%m/%d/', verbose_name="Resultados de análisis de laboratorio", null=True, blank=True)
	foto_recepcion = models.FileField(upload_to='pruebas/2/fotos/%Y/%m/%d/', verbose_name="Evidencia fotografica de recepción de muestra", null=True, blank=True)

	#Fase de Sugerencias / ECA(Pilar)
	resultados_IMTA = models.FileField(upload_to='pruebas/2/resultados/%Y/%m/%d/', verbose_name="Resultados de análisis para IMTA", null=True, blank=True)
	aprobacion_interna = models.FileField(upload_to='pruebas/2/resultados/%Y/%m/%d/', null=True, blank=True, verbose_name="Aprobación interna")

	#Fase de confirmación de IMTA
	dictamen_validacion = models.FileField(upload_to='pruebas/2/resultados/%Y/%m/%d/', verbose_name="Dictamen de validación", null=True, blank=True)
	aprobacion = models.CharField(max_length=11, default="En espera", choices=aprobacion_choices, verbose_name="Aprobación")

	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	laboratorio = models.ForeignKey(User, related_name="lab_segunda_prueba")
	
	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Segundas pruebas'