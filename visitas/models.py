from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class VisitaAlSitio(models.Model):
	escuela = models.OneToOneField(User)
	constancia_visita = models.FileField(upload_to='visitas/1/constancia/%Y/%m/%d/', verbose_name="Constancia de visita")
	hoja_cotizacion = models.FileField(upload_to='visitas/1/cotizacion/%Y/%m/%d/', verbose_name="Hoja de cotización")
	plantilla_fotografica = models.FileField(upload_to='visitas/1/plantilla/%Y/%m/%d/', verbose_name="Plantilla fotográfica")
	membrete_mail = models.FileField(upload_to='visitas/1/membrete/%Y/%m/%d/', verbose_name="Membrete para e-mail")
	agenda = models.FileField(upload_to='visitas/1/agenda/%Y/%m/%d/', verbose_name="Agenda")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	sim = models.ForeignKey(User, related_name="sim_primera_visita", null=True, blank=True)

	def __str__(self):
		return '{} para escuela'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Visitas al sitio'

class VisitaDeAcuerdo(models.Model):
	escuela = models.OneToOneField(User)
	acta_acuerdos = models.FileField(upload_to='visitas/2/acta/%Y/%m/%d/', verbose_name="Acta de acuerdos y ubicación del módulo")
	reporte_toma_agua = models.FileField(upload_to='visitas/2/reporte_de_toma/%Y/%m/%d/', verbose_name="Reporte de toma de muestra")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	sim = models.ForeignKey(User, related_name="sim_segunda_visita")

	def __str__(self):
		return '{} para escuela'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'visitas de acuerdos'

class EntregaDeBebedero(models.Model):
	escuela = models.OneToOneField(User)
	acta_entrega = models.FileField(upload_to='visitas/3/acta/%Y/%m/%d/', verbose_name="Acta de entrega de trabajos")
	convenio_responsabilidades = models.FileField(upload_to='visitas/3/responsabilidades/%Y/%m/%d/', verbose_name="Convenio de asignación de responsabilidades")
	constancia_entrega_llaves = models.FileField(upload_to='visitas/3/llaves/%Y/%m/%d/', verbose_name="Constancia de entrega de llaves")
	video  = models.FileField(upload_to='visitas/3/video/%Y/%m/%d/', verbose_name="Video de entrega de trabajos oficial al plantel y su correcto funcionamiento")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	sim = models.ForeignKey(User, related_name="sim_entrega_bebedero")

	def __str__(self):
		return '{} para escuela'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Entrega de bebederos'