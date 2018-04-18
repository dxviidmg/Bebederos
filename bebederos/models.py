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

	def __str__(self):
		return '{}'.format(self.tipo)
	
	class Meta:
		ordering = ['tipo']
		verbose_name_plural = 'Sistemas de potabilización'

class SistemaBebedero(models.Model):
	proveedor_choices = (
		("CRG", "CRG"),
		("KEVANCY", "KEVANCY"),
		("TAMA", "TAMA"),
	)

	status_choices = (
		("En proceso", "En proceso"),
		("Terminado", "Terminado"),
	)

	no_trazabilidad = models.CharField(max_length=100, null=True, blank=True)
	escuela = models.OneToOneField(User, related_name="escuela")
	mueble = models.ForeignKey(Mueble, related_name="mueble")
	proveedor = models.CharField(max_length=10, choices=proveedor_choices, default="CRG")
	no_serie_mueble = models.IntegerField(null=True, blank=True, verbose_name="No. de serie de mueble")
	sistema_potabilizacion = models.ForeignKey(SistemaPotabilizacion, related_name="sistema_potabilizacion",  null=True, blank=True, verbose_name="Sistema potabilizador")
	no_serie_sp = models.CharField(max_length=20, null=True, blank=True, verbose_name="No. de serie del sistema potabilizador ")
	capacidad_tanque_presurizador = models.IntegerField(null=True, blank=True, )
	asignacion = models.BooleanField(default=False, verbose_name="Si ya se descargó. imprimió y asignó la guia de trazabilidad al mueble correspondiente, oprima el botón")
	status = models.CharField(max_length=10, default="En proceso", choices=status_choices)
	
	def GenerateId(self):
		if self.sistema_potabilizacion and self.proveedor:
			cantidadCeros = 4-len(str(self.no_serie_mueble))
			no_serie_mueble = cantidadCeros*"0" + str(self.no_serie_mueble)
			hoy = datetime.today().strftime('%d%m%y')
			sistemaBebedero = SistemaBebedero.objects.get(pk=self.pk)
			escuela = User.objects.get(pk=sistemaBebedero.escuela.pk)
			entidad = escuela.perfil.municipio.zona.entidad
			no_trazabilidad = str(entidad.abreviatura) + "-" + str(sistemaBebedero.proveedor) + "-" + str(sistemaBebedero.mueble) + "-" + str(no_serie_mueble) + "-" + str(sistemaBebedero.sistema_potabilizacion) + "-" + str(hoy) + "-" + "T304" + "-" + str(escuela.username)
			self.no_trazabilidad = no_trazabilidad
			self.save()
		
	def CalculaCTP(self):
		sistemaBebedero = SistemaBebedero.objects.get(pk=self.pk)
		mueble = Mueble.objects.get(mueble=sistemaBebedero)
		totalSalidas = mueble.total_salidas
		if totalSalidas == 8:
			self.capacidad_tanque_presurizador = 5.5
		elif totalSalidas == 6:
			self.capacidad_tanque_presurizador = 4
		elif totalSalidas == 4 or totalSalidas == 3:
			self.capacidad_tanque_presurizador = 3		
		self.save()

	def __str__(self):
		return 'Bebedero {} para escuela {}'.format(self.mueble, self.escuela)
	
	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Sistemas bebedero'
