from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class PrimerVisita(models.Model):
	escuela = models.OneToOneField(User)
	constancia_de_visita = models.FileField(upload_to='visitas/1/constancia/%Y/%m/%d/', verbose_name="Constancia de visita")
	hoja_de_cotizacion = models.FileField(upload_to='visitas/1/cotizacion/%Y/%m/%d/', verbose_name="Hoja de cotizaciones")
	plantilla_fotografica = models.FileField(upload_to='visitas/1/plantilla/%Y/%m/%d/', verbose_name="Plantilla fotografica")
	membrete_para_mail = models.FileField(upload_to='visitas/1/membrete/%Y/%m/%d/', verbose_name="Membrete para e-mail")
	agenda = models.FileField(upload_to='visitas/1/agenda/%Y/%m/%d/', verbose_name="Agenda")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	sim = models.ForeignKey(User, related_name="sim_primera_visita", null=True, blank=True)

	def __str__(self):
		return '{} para escuela'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Primeras visitas'

class SegundaVisita(models.Model):
	escuela = models.OneToOneField(User)
	acta_acuerdos = models.FileField(upload_to='visitas/2/acta/%Y/%m/%d/', verbose_name="Acta de acuerdos y ubicación del módulo")
	reporte_de_toma = models.FileField(upload_to='visitas/2/reporte_de_toma/%Y/%m/%d/', verbose_name="Reporte de toma de muestra")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	sim = models.ForeignKey(User, related_name="sim_segunda_visita")

	def __str__(self):
		return '{} para escuela'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Segundas visitas'