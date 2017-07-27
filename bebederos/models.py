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
	cantidad_de_boquillas = models.IntegerField()
	cantidad_de_boquillas_discapacidad = models.IntegerField()
	cantidad_de_llenador_de_botellas = models.IntegerField()
	alumnos_min = models.IntegerField(null=True, blank=True)
	alumnos_max = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return '{} para escuela {}'.format(self.clave, self.nivel_educativo)

	class Meta:
		ordering = ['clave']

class SistemaPotabilizacion(models.Model):
	tipo = models.CharField(max_length=15, null=True, blank=True)
	descipcion = models.TextField(null=True, blank=True)
	litros_de_vida = models.IntegerField()

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
	identificador = models.IntegerField(default=0)
	escuela = models.OneToOneField(User, related_name="escuela")
	constructora = models.ForeignKey(User, related_name="constructora")
	mueble = models.ForeignKey(Mueble, related_name="mueble")
	sistema_de_potabilizacion = models.ForeignKey(SistemaPotabilizacion, null=True, blank=True)
	modulo = models.CharField(max_length=1, default="A", choices=modulo_choices)

	def __str__(self):
		return 'Bebedero {} para escuela {}'.format(self.mueble, self.escuela)
	
	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Sistemas bebederos'