from django.db import models
from django.contrib.auth.models import User

class Mueble(models.Model):
	nivel_educativo_choices = (
		("Preescolar", "Preescolar"),
		("Primaria", "Primaria"),
		("Secundaria", "Secundaria"),
		("Media Superior", "Media Superior"),
	)
	clave = models.CharField(max_length=10)
	nivel_educativo = models.CharField(max_length=30, choices=nivel_educativo_choices)
	cantidad_salidas_regulares = models.IntegerField()
	cantidad_salidas_discapacidad = models.IntegerField()
	cantidad_llenador_de_botellas = models.IntegerField()
	alumnos_min = models.IntegerField(null=True, blank=True, verbose_name="Rango minimo de alumnos")
	alumnos_max = models.IntegerField(null=True, blank=True, verbose_name="Rango maximo de alumnos")

	def __str__(self):
		return '{}'.format(self.clave)

	class Meta:
		ordering = ['clave']

class SistemaPotabilizacion(models.Model):
	tipo = models.CharField(max_length=15, null=True, blank=True)
	descipcion = models.TextField(null=True, blank=True, verbose_name="Descripción")
	litros_vida = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.tipo)
	
	class Meta:
		ordering = ['tipo']
		verbose_name_plural = 'Sistemas de potabilización'

class SistemaBebedero(models.Model):
	modulo_choices = (
		("A","A"),
		("B","B"),
	)
	identificador_mb = models.CharField(max_length=20, null=True, blank=True, verbose_name="Identificador de mueble bebedero")
	escuela = models.OneToOneField(User, related_name="escuela")
	ejecutora = models.ForeignKey(User, related_name="Ejecutora", null=True, blank=True)
	mueble = models.ForeignKey(Mueble, related_name="mueble")
	sistema_de_potabilizacion = models.ForeignKey(SistemaPotabilizacion, null=True, blank=True)
	identificador_sp = models.CharField(max_length=20, null=True, blank=True, verbose_name="Identificador de sistema de potabilización")
	qr_sp = models.FileField(upload_to='codigos/sp/%Y/%m/%d/', verbose_name="Codigo QR de sistema de potabilización", null=True, blank=True)	
	modulo = models.CharField(max_length=1, default="A", choices=modulo_choices)

	def __str__(self):
		return 'Bebedero {} para escuela {}'.format(self.mueble, self.escuela)
	
	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Sistemas bebedero'