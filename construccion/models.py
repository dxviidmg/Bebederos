from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class InicioDeTrabajo(models.Model):
	escuela = models.OneToOneField(User, related_name="escuela_inicio_trabajo")
	acta_inicio = models.FileField(upload_to='iniciosTrabajo/actas/%Y/%m/%d/', verbose_name="Acta de inicio de trabajo")

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Inicio de trabajos'

class EnvolventeTerminada(models.Model):
	escuela = models.OneToOneField(User, related_name="escuela_instalacion_bebedero")
	video = models.FileField(upload_to='evidencia/envolvente/%Y/%m/%d/', verbose_name="Video")

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Envolventes terminadas'

class EvidenciaConstruccion(models.Model):
	fase_choices = (
		("1° Trazo", "1° Trazo"),
		("2° Excavación, corte y demolición", "2° Excavación, corte y demolición"),
		("3° Cimbra y habilitado de firme", "3° Cimbra y habilitado de firme"),
		("4° Colado de firme", "4° Colado de firme"),
		("5° Muros, castillos y cadenas" , "5° Muros, castillos y cadenas"),
		("6° Aplanados, pinturas y rampa", "6° Aplanados, pinturas y rampa"),
		("7° Estructura y puerta", "7° Estructura y puerta"),
		("8° Policarbonato", "8° Policarbonato"),
		("9° Mueble bebedero", "9° Mueble bebedero"),
		("10° Placa de identidad", "10° Placa de identidad"),
	)

	aprobacion_choices = (
		("En espera", "En espera"),
		("Aprobado", "Aprobado"),
		("No aprobado", "No aprobado"),
	)

	escuela = models.ForeignKey(User, related_name="escuela_evidencia")
	fase = models.CharField(max_length=50, choices=fase_choices)
	foto = models.FileField(upload_to='evidencia/foto/%Y/%m/%d/', verbose_name="Fotografía")
	aprobacion_SI = models.CharField(max_length=11, default="En espera", choices=aprobacion_choices, verbose_name="Aprobación del Superintendente")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")

	def __str__(self):
		return 'Fase {} de {}'.format(self.fase, self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Evidencias de construcción'


