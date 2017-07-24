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
	salidas = models.IntegerField()
	rango = models.CharField(max_length=10)

	def __str__(self):
		return '{} para escuela {}'.format(self.clave, self.nivel_educativo)

	class Meta:
		ordering = ['clave']

class Filtro(models.Model):
	normas_choices = (
		("NOM-127-SSA1-1994","NOM-127-SSA1-1994"),
		("NOM-201-SSA1-2015","NOM-201-SSA1-2015"),
		("Ambas","Ambas"),
		("Ninguna","Ninguna"),
	)
	modelo = models.CharField(max_length=10)
	litros_de_vida = models.IntegerField()
	presion = models.CharField(max_length=30, verbose_name="Presión")
	normas_cumplidas = models.CharField(max_length=20, choices=normas_choices)

	def __str__(self):
		return 'Modelo {}'.format(self.modelo)
	
	class Meta:
		ordering = ['modelo']

class SistemaBebedero(models.Model):

	modulo_choices = (
		("A","A"),
		("B","B"),
	)

	identificador = models.IntegerField(default=0)
	escuela = models.OneToOneField(User, related_name="escuela")
	constructora = models.ForeignKey(User, related_name="constructora")
	mueble = models.ForeignKey(Mueble, related_name="mueble")
	filtro = models.ForeignKey(Filtro, related_name="filtro")
	modulo = models.CharField(max_length=1, default="A", choices=modulo_choices)

	def __str__(self):
		return 'Bebedero {} para escuela {}'.format(self.mueble, self.escuela)
	
	class Meta:
		ordering = ['escuela']