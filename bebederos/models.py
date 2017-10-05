from django.db import models
from django.contrib.auth.models import User

class Mueble(models.Model):
	nivel_educativo_choices = (
		("Preescolar", "Preescolar"),
		("Primaria", "Primaria"),
		("Secundaria", "Secundaria"),
	)

	clave = models.CharField(max_length=10)
	nivel_educativo = models.CharField(max_length=30, choices=nivel_educativo_choices)
	cantidad_salidas_regulares = models.IntegerField()
	cantidad_salidas_discapacidad = models.IntegerField()
	cantidad_llenador_de_botellas = models.IntegerField()
	alumnos_min = models.IntegerField(verbose_name="Rango minimo de alumnos")
	alumnos_max = models.IntegerField(verbose_name="Rango maximo de alumnos")

	def __str__(self):
		return '{}'.format(self.clave)

	class Meta:
		ordering = ['clave']

class SistemaPotabilizacion(models.Model):
	tipo = models.CharField(max_length=15)
	descripcion = models.TextField(verbose_name="Descripción")
	litros_vida = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.tipo)
	
	class Meta:
		ordering = ['tipo']
		verbose_name_plural = 'Sistemas de potabilización'

class SistemaBebedero(models.Model):
	linea_ensamblaje_choices = [(str(i), i) for i in range(1,7)]

	identificador = models.CharField(max_length=100, null=True, blank=True)
	escuela = models.OneToOneField(User, related_name="escuela")
	mueble = models.ForeignKey(Mueble, related_name="mueble")
	sistema_de_potabilizacion = models.ForeignKey(SistemaPotabilizacion, related_name="sistema_potabilizacion",  null=True, blank=True)
	identificador_sp = models.CharField(max_length=20, null=True, blank=True, verbose_name="Identificador de sistema de potabilización")
	componentes_sp = models.CharField(max_length=30, null=True, blank=True, verbose_name="Componentes del sistema de potabilización")
	linea_ensamblaje = models.CharField(max_length=5, choices=linea_ensamblaje_choices, null=True, blank=True)
	ejecutora = models.ForeignKey(User, related_name="ejecutora", null=True, blank=True)
	
	def __str__(self):
		return 'Bebedero {} para escuela {}'.format(self.mueble, self.escuela)
	
	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Sistemas bebedero'