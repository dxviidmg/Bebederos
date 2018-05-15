from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from pruebasAgua.models import PrimerPrueba
from construccion.models import EvidenciaConstruccion
from geoposition.fields import GeopositionField
from mantenimiento.models import *

class Region(models.Model):
	coordinador_regional_inifed = models.OneToOneField(User, null=True, blank=True, verbose_name="Coordinador Regional de INIFED", related_name="coordinador_regional_inifed")
	enlace_institucional_inifed = models.OneToOneField(User, null=True, blank=True, verbose_name="Enlace Institucional de INIFED", related_name="enlace_institucional_inifed")	
	nombre = models.CharField(max_length=20)
	numero = models.IntegerField()
	color = models.CharField(max_length=10, verbose_name="Color (Hexadecimal o en inglés)")

	def __str__(self):
		return '{} {}'.format(self.numero, self.nombre)

	class Meta:
		ordering = ['numero']
		verbose_name_plural = "Regiones"

class Entidad(models.Model):
	region = models.ForeignKey(Region, verbose_name="Región")
	partida = models.IntegerField(verbose_name="Partida")

	#Perfiles de INIFED
	coordinador_estatal_inifed = models.OneToOneField(User, null=True, blank=True, verbose_name="Coordinador Estatal de INIFED", related_name="coordinador_estatal_inifed")
#	residente_tecnico_inifed = models.ForeignKey(User, null=True, blank=True, verbose_name="Residente Técnico de INIFED", related_name="residente_tecnico_inifed")

	#Perfiles de Residente
	superintendente = models.OneToOneField(User, null=True, blank=True, verbose_name="Superintendente", related_name="superintendente")
	sim = models.OneToOneField(User, null=True, blank=True, verbose_name="Superintendente de mantenimiento", related_name="sim")

	laboratorio = models.ForeignKey(User, null=True, blank=True, verbose_name="Laboratorio", related_name="laboratorio")

	nombre = models.CharField(max_length=100)
	abreviatura = models.CharField(max_length=4)
	escuelas_asignadas = models.IntegerField(default=0)
	escuelas_registradas = models.IntegerField(default=0)
	imagen = models.ImageField(upload_to='estados/%Y/%m/%d/', default='img_no_disponible.jpg')
	slug = models.SlugField(null=True)
	t7 = models.FileField(upload_to='t7/%Y/%m/%d/', verbose_name="Archivo(s) de T7", null=True, blank=True)

	def CountEscuelas(self):
		entidad = Entidad.objects.get(pk=self.pk)
		zonas = Zona.objects.filter(entidad=entidad)
		municipios = Municipio.objects.filter(zona__in=zonas)
		escuelas_registradas_count = Perfil.objects.filter(municipio__in=municipios).count()	
		self.escuelas_registradas = escuelas_registradas_count
		self.save()

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['partida', 'nombre']
		verbose_name_plural = "Entidades"

	def get_absolute_url(self):
		return reverse('accounts:ListViewMunicipios', kwargs={'numero': self.partida.numero, 'slug': self.slug})

class Zona(models.Model):
	entidad = models.ForeignKey(Entidad)
	nombre = models.CharField(max_length=30, verbose_name="Nombre o número")
	color = models.CharField(max_length=30, verbose_name="Color (Hexadecimal o en inglés)")

	def __str__(self):
		return '{} de {}'.format(self.nombre, self.entidad)

	class Meta:
		ordering = ['entidad', 'nombre']

class Municipio(models.Model):
	zona = models.ForeignKey(Zona, null=True)
	nombre = models.CharField(max_length=100)
	escuelas_registradas = models.IntegerField(default=0)
	slug = models.SlugField(null=True)

	def CountEscuelas(self):
		municipio = Municipio.objects.get(pk=self.pk)
		escuelas_registradas_count = Perfil.objects.filter(municipio=municipio).count()
		self.escuelas_registradas = escuelas_registradas_count
		self.save()

	def __str__(self):
		return '{} de Zona {}'.format(self.nombre, self.zona)

	class Meta:
		ordering = ['nombre']

class Perfil(models.Model):
	tipo_choices = (
		("Administrador", "Administrador"), #Yo
		("Ejecutora", "Ejecutora"),
		("Escuela", "Escuela"),
		("Laboratorio", "Laboratorio"),
		("INIFED", "INIFED"), #INIFED Federal
		("PQ", "Procesos Químicos (Calidad de Agua)"), #Pilar, #Isauri
		("PM", "Planta y Manufactura"), #Raúl, Héctor
		("Invitado", "Invitado"), #Raúl, Héctor
	)

	nivel_choices = (
		("Preescolar", "Preescolar"),
		("Primaria", "Primaria"),
		("Secundaria", "Secundaria"),
	)

	turno_choices = (
		("Matutino", "Matutino"),
		("Vespertino", "Vespertino"),
		("Tiempo Completo", "Tiempo Completo"),
	)

	cargo_choices = (
		('INIFED', (
				('CRINIFED', 'Coordinador Regional'),
				('EIINIFED', 'Enlace Institucional'),
				('CEINIFED', 'Coordinador Estatal'),
				('RTINIFED', 'Residente Técnico'),
			)
		),
		('Ejecutora', (
				('SIM', 'Superintendente de Mantenimiento'),			
				('SI', 'Superintendente'),
				('RO', 'Residente de Obra'),				
			)
		)
	)

	#Atributos de todos los usuarios, sin importar el tipo
	user = models.OneToOneField(User)
	telefono = models.CharField(max_length=25, blank=True, null=True, verbose_name="Teléfono")
	tipo = models.CharField(max_length=30, choices=tipo_choices)
	cargo = models.CharField(max_length=30, blank=True, null=True, verbose_name="Cargo", choices=cargo_choices)

	#Atributos exclusivos de escuelas
	municipio = models.ForeignKey(Municipio, null=True, blank=True)
	director = models.CharField(max_length=100, blank=True, null=True)
	foto_escuela = models.ImageField(upload_to='fotos/escuela/%Y/%m/%d/', null=True, blank=True, verbose_name="Foto de la entrada de la escuela")
	nivel_educativo = models.CharField(max_length=20, blank=True, null=True, choices=nivel_choices)
	turno = models.CharField(max_length=20, blank=True, null=True, choices=turno_choices)
	plantilla_escolar = models.IntegerField(blank=True, null=True)
	avance = models.IntegerField(blank=True, null=True)
	domicilio = models.CharField(max_length=400, blank=True, null=True)
	localidad = models.CharField(max_length=200, blank=True, null=True)
	referencias = models.CharField(max_length=200, blank=True, null=True)
	SSID = models.CharField(max_length=20, null=True, blank=True)
	clave_SSID = models.CharField(max_length=20, null=True, blank=True)
	coordenadas = GeopositionField(null=True, blank=True)
	mantenimientos = models.IntegerField(null=True, blank=True)
	evidencias = models.IntegerField(null=True, blank=True)

	#Llave foranea para Residentes Técnicos de INIFED
	residente_tecnico_inifed = models.ForeignKey(Entidad, verbose_name="Es residente estatal de INIFED del estado de", null=True, blank=True, related_name="residente_tecnico_inifed")
	residente_obra_ejecutora = models.ForeignKey(Entidad, verbose_name="Es residente de obra de la ejecutora del estado de", null=True, blank=True, related_name="residente_obra_ejecutora")

	def UpdateAvance(self):
		perfil = Perfil.objects.get(pk=self.pk)
		escuela = User.objects.get(perfil=perfil)
		ultimaEvidencia = EvidenciaConstruccion.objects.filter(escuela=escuela).order_by('pk').last()

		if ultimaEvidencia.fase == "1° Trazo" and ultimaEvidencia.aprobacion_SI == "Aprobado":
			self.avance = 10
			self.save()
		elif ultimaEvidencia.fase == "2° Excavación, corte y demolición" and ultimaEvidencia.aprobacion_SI == "Aprobado":
			self.avance = 20
			self.save()
		elif ultimaEvidencia.fase == "3° Cimbra y habilitado de firme" and ultimaEvidencia.aprobacion_SI == "Aprobado":
			self.avance = 30
			self.save()
		elif ultimaEvidencia.fase == "4° Colado de firme" and ultimaEvidencia.aprobacion_SI == "Aprobado":
			self.avance = 40
			self.save()
		elif ultimaEvidencia.fase == "5° Muros, castillos y cadenas" and ultimaEvidencia.aprobacion_SI == "Aprobado":
			self.avance = 50
			self.save()
		elif ultimaEvidencia.fase == "6° Aplanados, pinturas y rampa" and ultimaEvidencia.aprobacion_SI == "Aprobado":
			self.avance = 60
			self.save()
		elif ultimaEvidencia.fase == "7° Estructura y puerta" and ultimaEvidencia.aprobacion_SI == "Aprobado":
			self.avance = 70
			self.save()
		elif ultimaEvidencia.fase == "8° Policarbonato" and ultimaEvidencia.aprobacion_SI == "Aprobado":
			self.avance = 80
			self.save()			
		elif ultimaEvidencia.fase == "9° Mueble bebedero" and ultimaEvidencia.aprobacion_SI == "Aprobado":
			self.avance = 90
			self.save()
		elif ultimaEvidencia.fase == "10° Placa de identidad" and ultimaEvidencia.aprobacion_SI == "Aprobado":
			self.avance = 100
			self.save()

	def UpdateMantenimientosCount(self):
		perfil = Perfil.objects.get(pk=self.pk)
		escuela = User.objects.get(perfil=perfil)
		mantenimientos = Mantenimiento.objects.filter(escuela=escuela).count()
		self.mantenimientos = mantenimientos
		self.save()

	def UpdateEvidenciasCount(self):
		perfil = Perfil.objects.get(pk=self.pk)
		escuela = User.objects.get(perfil=perfil)
		evidencias = EvidenciaConstruccion.objects.filter(escuela=escuela).count()
		self.evidencias = evidencias
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