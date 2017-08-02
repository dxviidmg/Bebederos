from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from bebederos.models import *

class Region(models.Model):
	numero = models.IntegerField()
	color = models.CharField(max_length=10)

	def __str__(self):
		return '{}'.format(self.numero)

	class Meta:
		ordering = ['numero']
		verbose_name_plural = "Regiones"

	def get_absolute_url(self):
		return reverse('accounts:ListViewPartidas', kwargs={'numero': self.numero})

class Partida(models.Model):
	region = models.ForeignKey(Region, verbose_name="Región")
	numero = models.IntegerField(verbose_name="número")

	def __str__(self):
		return 'Partida {} de la región {}'.format(self.numero, self.region)	

class Entidad(models.Model):
	representante_inifed = models.ForeignKey(User, null=True, blank=True)
	partida = models.ForeignKey(Partida)
	nombre = models.CharField(max_length=30, verbose_name="número")
	slug = models.SlugField(null=True)
	imagen = models.ImageField(upload_to='estados/%Y/%m/%d/', default='img_no_disponible.jpg')

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['partida']
		verbose_name_plural = "Entidades"

	def get_absolute_url(self):
		return reverse('accounts:ListViewMunicipios', kwargs={'numero': self.partida.numero, 'slug': self.slug})

class Zona(models.Model):
	sim = models.ForeignKey(User, null=True, blank=True)
	entidad = models.ForeignKey(Entidad)
	nombre = models.CharField(max_length=30)
	color = models.CharField(max_length=30, default="#fff")

	def __str__(self):
		return '{}, {}'.format(self.nombre, self.entidad)

class Municipio(models.Model):
	zona = models.ForeignKey(Zona, null=True)
	nombre = models.CharField(max_length=30)
	slug = models.SlugField(null=True)

	def __str__(self):
		return '{}, Zona {}'.format(self.nombre, self.zona)

	class Meta:
		ordering = ['nombre']

class Perfil(models.Model):
	tipo_choices = (
		("Administrador", "Administrador"),
		("Residente", "Residente"),
		("SIM", "SIM"),
		("Ejecutora", "Ejecutora"),
		("Escuela", "Escuela"),
		("Laboratorio", "Laboratorio"),
		("INIFED Estatal", "INIFED Estatal"),
	)

	nivel_choices = (
		("Preescolar", "Preescolar"),
		("Primaria", "Primaria"),
		("Secundaria", "Secundaria"),
		("Media Superior", "Media Superior"),
		("Superior", "Superior"),
	)

	conexion_choices = (
		("Red Municipal", "Red Municipal"),
		("No especificado", "No especificado"),
	)

	turno_choices = (
		("Matutino", "Matutino"),
		("Vespertino", "Vespertino"),
	)

	user = models.OneToOneField(User)
	tipo = models.CharField(max_length=30, choices=tipo_choices)
	telefono = models.CharField(max_length=10, blank=True, null=True, verbose_name="Teléfono")
	domicilio = models.CharField(max_length=100, blank=True, null=True)
	referencias = models.CharField(max_length=200, blank=True, null=True)

	#Atributos exclusivos de escuelas
	municipio = models.ForeignKey(Municipio, null=True, blank=True)	
	director = models.CharField(max_length=100, blank=True, null=True)
	foto_director = models.ImageField(upload_to='fotos/director/%Y/%m/%d/', null=True, blank=True)
	nivel_educativo = models.CharField(max_length=20, blank=True, null=True, choices=nivel_choices)
	turno = models.CharField(max_length=20, blank=True, null=True, choices=turno_choices)
	plantilla_escolar = models.IntegerField(blank=True, null=True)
	conexion = models.CharField(max_length=20, blank=True, null=True, choices=conexion_choices)
	aulas_existentes = models.IntegerField(blank=True, null=True)
	aulas_en_uso = models.IntegerField(blank=True, null=True)
	status = models.CharField(max_length=20, default='Por definir')

	#Clave de constructora para escuela
	clave = models.CharField(max_length=6, blank=True, null=True)

	representante_legal = models.CharField(max_length=100, blank=True, null=True)

	def UpdateStatus(self):
		perfil = Perfil.objects.get(pk=self.pk)
		escuela = User.objects.get(perfil=perfil)
		sistemabebedero = SistemaBebedero.objects.get(escuela=escuela)
		dictamen = EvidenciaPrevia.objects.filter(sistemabebedero=sistemabebedero).last()

		if dictamen.nombre == "Validación de la calidad del agua" and dictamen.aprobacion_imta == "Aprobado":
			self.status = "Aceptado"
		elif dictamen.nombre == "Validación de la calidad del agua" and dictamen.aprobacion_imta == "No aprobado":
			self.status = "Rechazado"
		self.save()

	def __str__(self):
		return '{} {} {}'.format(self.tipo, self.user.first_name, self.user.last_name)

	class Meta:
		ordering = ['user']
		verbose_name_plural = "Perfiles"

#Muestra nombre completo	
def get_full_name(self):
	return '{} {}'.format(self.first_name, self.last_name)

User.add_to_class("__str__", get_full_name)