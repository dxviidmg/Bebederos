from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from accounts.models import *

class Mueble(models.Model):
	nivel_educativo_choices = (
		("Preescolar", "Preescolar"),
		("Primaria", "Primaria"),
		("Secundaria", "Secundaria"),
	)

	modelo = models.CharField(max_length=10)
	nivel_educativo = models.CharField(max_length=30, choices=nivel_educativo_choices)
	salidas_regulares = models.IntegerField()
	salidas_discapacidad = models.IntegerField()
	llenador_botellas = models.IntegerField()
	total_salidas = models.IntegerField()
	alumnos_min = models.IntegerField(verbose_name="Rango minimo de alumnos")
	alumnos_max = models.IntegerField(verbose_name="Rango maximo de alumnos")

	def __str__(self):
		return '{}'.format(self.modelo)

	class Meta:
		ordering = ['modelo']

class SistemaPotabilizacion(models.Model):
	tipo = models.CharField(max_length=15)
	descripcion = models.TextField(verbose_name="Descripción")
	litros_vida = models.IntegerField(verbose_name="Litrso de vida")

	def __str__(self):
		return '{}'.format(self.tipo)
	
	class Meta:
		ordering = ['tipo']
		verbose_name_plural = 'Sistemas de potabilización'

class SistemaBebedero(models.Model):
	linea_ensamblaje_choices = [(str(i), i) for i in range(1,7)]

	no_trazabilidad = models.CharField(max_length=100, null=True, blank=True)
	escuela = models.OneToOneField(User, related_name="escuela")
	mueble = models.ForeignKey(Mueble, related_name="mueble")
	sistema_potabilizacion = models.ForeignKey(SistemaPotabilizacion, related_name="sistema_potabilizacion",  null=True, blank=True)
	identificador_sp = models.CharField(max_length=20, null=True, blank=True, verbose_name="Identificador de sistema de potabilización")
	componentes_sp = models.CharField(max_length=30, null=True, blank=True, verbose_name="Componentes del sistema de potabilización")
	linea_ensamblaje = models.CharField(max_length=5, choices=linea_ensamblaje_choices, null=True, blank=True)
	ejecutora = models.ForeignKey(User, related_name="ejecutora", null=True, blank=True)
	asignacion = models.BooleanField(default=False, verbose_name="Si ya se descargó. imprimió y asignó la guia de trazabilidad al mueble correspondiente, oprima el botón")

	def GenerateId(self):
		if self.sistema_potabilizacion and self.linea_ensamblaje:
			cantidadCeros = 4-len(str(self.pk))
			serie = cantidadCeros*"0" + str(self.pk)
			hoy = datetime.today().strftime('%d%m%y')
			sistemaBebedero = SistemaBebedero.objects.get(pk=self.pk)
			escuela = User.objects.get(pk=sistemaBebedero.escuela.pk)
			entidad = escuela.perfil.municipio.zona.entidad
			no_trazabilidad = str(entidad.abreviatura) + str(sistemaBebedero.mueble) + str(sistemaBebedero.sistema_potabilizacion) + str(serie) + str(hoy) + "T304" + str(sistemaBebedero.linea_ensamblaje) + str(escuela.username)
			self.no_trazabilidad = no_trazabilidad
			self.save()
		

	def __str__(self):
		return 'Bebedero {} para escuela {}'.format(self.mueble, self.escuela)
	
	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Sistemas bebedero'
