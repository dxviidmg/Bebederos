from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Region(models.Model):
	numero = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.numero)

	class Meta:
		ordering = ['numero']
		verbose_name_plural = "Regiones"

	def get_absolute_url(self):
		return reverse('accounts:ListViewEntidades', kwargs={'numero': self.numero})

class Entidad(models.Model):
	region = models.ForeignKey(Region)
	partida = models.IntegerField()
	nombre = models.CharField(max_length=30)
	slug = models.SlugField(null=True)
	imagen = models.ImageField(upload_to='estados/%Y/%m/%d/', default='img_no_disponible.jpg')

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['region', 'partida']
		verbose_name_plural = "Entidades"

	def get_absolute_url(self):
		return reverse('accounts:ListViewMunicipios', kwargs={'numero': self.region.numero, 'slug': self.slug})

class Municipio(models.Model):
	entidad = models.ForeignKey(Entidad)
	nombre = models.CharField(max_length=30)
	slug = models.SlugField(null=True)

	def __str__(self):
		return '{}, {}'.format(self.entidad, self.nombre)

	class Meta:
		ordering = ['entidad', 'nombre']

class Perfil(models.Model):
	tipo_choices = (
		("Administrador", "Administrador"),
		("Residente", "Residente"),
		("SIM", "SIM"),
		("Ejecutora", "Ejecutora"),
		("Escuela", "Escuela"),
	)
	user = models.OneToOneField(User)
	tipo = models.CharField(max_length=30, choices=tipo_choices)
	telefono = models.CharField(max_length=10, blank=True, null=True)
	domicilio = models.CharField(max_length=100, blank=True, null=True)
	municipio = models.ForeignKey(Municipio, null=True, blank=True)
	cantidad_de_alumnos = models.IntegerField(blank=True, null=True)
	director = models.CharField(max_length=100, blank=True, null=True)
	representante_legal = models.CharField(max_length=100, blank=True, null=True)
	
	def __str__(self):
		return '{} {} {}'.format(self.tipo, self.user.first_name, self.user.last_name)

	class Meta:
		ordering = ['user']

#Muestra nombre completo	
def get_full_name(self):
	return '{} {}'.format(self.first_name, self.last_name)

User.add_to_class("__str__", get_full_name)