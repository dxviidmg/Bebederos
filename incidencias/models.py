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
		("Baja", "Baja"),
		("Media", "Media"),
		("Alta", "Alta"),
	)
	etapa_choices = (
		("Formalidades (Pre-construcción)", "Formalidades (Pre-construcción)"),
		("Pruebas de calidad de agua", "Pruebas de calidad de agua"),
		("Construcción e instalación de Sistema bebedero", "Construcción e instalación de Sistema bebedero"),
		("Entrega del sistema bebedero", "Entrega del sistema bebedero"),
		("Mantenimiento", "Mantenimiento"),
	)
	escuela = models.ForeignKey(User, related_name="escuela_incidencia")
	autor = models.ForeignKey(User, related_name="autor")
	descripcion = models.TextField()
	status = models.CharField(default="En espera", max_length=30, choices=status_choices)
	prioridad = models.CharField(choices=prioridad_choices, max_length=5)
	etapa = models.CharField(choices=etapa_choices, max_length=100)
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")

	def __str__(self):
		return '{} para escuela'.format(self.escuela)

	class Meta:
		ordering = ['creacion']
#		verbose_name_plural = 'Terminos de trabajo'