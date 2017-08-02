from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Incidencia(models.Model):
	status_choices = (
		(1, "En espera"),
		(2, "En proceso de solución"),
		(3, "Solucionado"),
	)
	prioridad_choices = (
		(1, "Baja"),
		(2, "Media"),
		(3, "Alta"),
	)
	etapa_choices = (
		(1, "Formalidades (Pre-construcción)"),
		(2, "Construcción e instalación de Sistema bebedero"),
		(3, "Entrega del sistema bebedero"),
		(4, "Mantenimiento"),
	)
	escuela = models.ForeignKey(User, related_name="escuela_incidencia")
	autor = models.ForeignKey(User, related_name="autor")
	descripcion = models.TextField()
	status = models.IntegerField(default=1, choices=status_choices)
	prioridad = models.IntegerField(choices=prioridad_choices)
	etapa = models.IntegerField(choices=etapa_choices)
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")

	def __str__(self):
		return '{} para escuela'.format(self.escuela)

	class Meta:
		ordering = ['creacion']
#		verbose_name_plural = 'Terminos de trabajo'