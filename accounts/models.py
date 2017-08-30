from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from pruebasAgua.models import PrimerPrueba
from construccion.models import EvidenciaConstruccion

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
		return '{} de región {}'.format(self.numero, self.region)	

	class Meta:
		ordering = ['region', 'numero']

class Entidad(models.Model):
	representante_inifed = models.ForeignKey(User, null=True, blank=True)
	partida = models.ForeignKey(Partida)
	nombre = models.CharField(max_length=30)
	slug = models.SlugField(null=True)
	imagen = models.ImageField(upload_to='estados/%Y/%m/%d/', default='img_no_disponible.jpg')

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['partida', 'nombre']
		verbose_name_plural = "Entidades"

	def get_absolute_url(self):
		return reverse('accounts:ListViewMunicipios', kwargs={'numero': self.partida.numero, 'slug': self.slug})

class Zona(models.Model):
	sim = models.ForeignKey(User, null=True, blank=True, verbose_name="SIM")
	entidad = models.ForeignKey(Entidad)
	nombre = models.CharField(max_length=30, verbose_name="Nombre o número")
	color = models.CharField(max_length=30)

	def __str__(self):
		return '{} de {}'.format(self.nombre, self.entidad)

	class Meta:
		ordering = ['entidad', 'nombre']

class Municipio(models.Model):
	zona = models.ForeignKey(Zona, null=True)
	nombre = models.CharField(max_length=30)
	slug = models.SlugField(null=True)

	def __str__(self):
		return '{} de Zona {}'.format(self.nombre, self.zona)

	class Meta:
		ordering = ['nombre']

class Perfil(models.Model):
	tipo_choices = (
		("Administrador", "Administrador"),
		("SIM", "SIM"),
		("Ejecutora", "Ejecutora"),
		("Escuela", "Escuela"),
		("Laboratorio", "Laboratorio"),
		("INIFED", "INIFED"),
		("IMTA", "IMTA"),
		("ECA", "Residente Técnico de Calidad de Agua")
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
	status = models.CharField(max_length=20, blank=True, null=True)
	avance = models.IntegerField(blank=True, null=True)

	#Atributo exclusivo para Constructoras
	representante_legal = models.CharField(max_length=100, blank=True, null=True)

	def UpdateStatus(self):
		perfil = Perfil.objects.get(pk=self.pk)
		escuela = User.objects.get(perfil=perfil)
		primerPrueba = PrimerPrueba.objects.get(escuela=escuela)
		
		if primerPrueba.aprobacion == "Aprobado":
			self.status = "Aceptado"
		elif primerPrueba.aprobacion == "No aprobado":
			self.status = "Rechazado"
			self.save()

	def UpdateAvance(self):
		perfil = Perfil.objects.get(pk=self.pk)
		escuela = User.objects.get(perfil=perfil)

		primerPrueba = PrimerPrueba.objects.get(escuela=escuela)
		ultimaEvidencia = EvidenciaConstruccion.objects.filter(escuela=escuela).order_by('pk').last()

		if primerPrueba.aprobacion == "Aprobado": 
			if ultimaEvidencia == None:
				self.avance = 0
				self.save()
			else:
				if ultimaEvidencia.fase == "Firme" and ultimaEvidencia.aprobacion == "Aprobado":
					self.avance = 25
					self.save()
				elif ultimaEvidencia.fase == "Muro" and ultimaEvidencia.aprobacion == "Aprobado":
					self.avance = 50
					self.save()					
				elif ultimaEvidencia.fase == "Techumbre y puerta" and ultimaEvidencia.aprobacion == "Aprobado":
					self.avance = 75
					self.save()
				elif ultimaEvidencia.fase == "Instalación de Mueble Bebedero" and ultimaEvidencia.aprobacion == "Aprobado":
					self.avance = 100
					self.save()
#			if bitacora.fase == "Firme":
#				self.avance == 25
#				self.save()

	def __str__(self):
		return '{} {} {}'.format(self.tipo, self.user.first_name, self.user.last_name)

	class Meta:
		ordering = ['user']
		verbose_name_plural = "Perfiles"

#Muestra nombre completo	
def get_full_name(self):
	return '{} {}'.format(self.first_name, self.last_name)

User.add_to_class("__str__", get_full_name)