from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Incidencia(models.Model):
	status_choices = (
		("En espera", "En espera"),
		("Atendiendo", "Atendiendo"),
		("Solucionado", "Solucionado"),
	)
	prioridad_choices = (
		("Ninguna", "Ninguna (Es una notificación)"),
		("Baja", "Baja"),
		("Media", "Media"),
		("Alta", "Alta"),
	)
	fase_choices = (
		("Primer prueba de calidad de agua", "Primer prueba de calidad de agua"),
		("Inicio de trabajo", "Inicio de trabajo"),	
		("Visita de acuerdos", "Visita de acuerdos"),
		("Construcción e instalación de Sistema bebedero", "Construcción e instalación de Sistema bebedero"),
		("Segunda prueba de calidad de agua", "Segunda prueba de calidad de agua"),	
		("Inicio de funcionamiento", "Inicio de funcionamiento"),
		("Mantenimiento", "Mantenimiento"),
	)

	autor = models.ForeignKey(User, related_name="autor")
	descripcion = models.TextField(verbose_name="Descripción")
	status = models.CharField(default="En espera", max_length=30, choices=status_choices)
	prioridad = models.CharField(choices=prioridad_choices, max_length=10)
	fase = models.CharField(choices=fase_choices, max_length=100)
	solucion = models.TextField(verbose_name="Solución", null=True, blank=True)
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	escuela = models.ForeignKey(User, related_name="escuela_incidencia", null=True, blank=True)
	evidencia = models.ImageField(upload_to="incidencias/%Y/%m/%d/", null=True, blank=True, verbose_name="Evidencia fotográfica de incidencia")
	evidencia_2 = models.ImageField(upload_to="incidencias/%Y/%m/%d/", null=True, blank=True, verbose_name="Evidencia fotográfica de solución")

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['creacion']