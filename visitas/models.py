from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class VisitaAlSitio(models.Model):
	escuela = models.OneToOneField(User)
	acta_visita = models.FileField(upload_to='visitas/1/acta/%Y/%m/%d/', verbose_name="Acta de visita", null=True, blank=True)
	copia_INE = models.FileField(upload_to='visitas/1/INE/%Y/%m/%d/', verbose_name="Copia de INE", null=True, blank=True)
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	si = models.ForeignKey(User, related_name="si_primera_visita", null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Visitas al sitio'

class VisitaDeAcuerdo(models.Model):
	escuela = models.OneToOneField(User)
	convenio_concertacion = models.FileField(upload_to='visitas/2/concertacion/%Y/%m/%d/', verbose_name="Convenio de concertación de aplicación de recurso", null=True, blank=True)
	cedula_identificacion = models.FileField(upload_to='visitas/2/identificacion/%Y/%m/%d/', verbose_name="Cédula de identificación basica", null=True, blank=True)
	acta_acuerdos = models.FileField(upload_to='visitas/2/acta/%Y/%m/%d/', verbose_name="Acta de acuerdos y ubicación del módulo")
	constancia_integracion_comite = models.FileField(upload_to='visitas/2/comite/%Y/%m/%d/', verbose_name="Constancia de Integración de Comité", null=True, blank=True)
	acta_inicio_reportes = models.FileField(upload_to='visitas/2/reportes/%Y/%m/%d/', verbose_name="Acta de inicio de reportes", null=True, blank=True)
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	si = models.ForeignKey(User, related_name="si_segunda_visita", null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Visitas de acuerdo'

class EntregaDeBebedero(models.Model):
	escuela = models.OneToOneField(User)
	acta_entrega = models.FileField(upload_to='visitas/3/acta/%Y/%m/%d/', verbose_name="Acta de entrega de trabajos")
	convenio_responsabilidades = models.FileField(upload_to='visitas/3/responsabilidades/%Y/%m/%d/', verbose_name="Convenio de asignación de responsabilidades")
	constancia_entrega_llaves = models.FileField(upload_to='visitas/3/llaves/%Y/%m/%d/', verbose_name="Constancia de entrega de llaves")
	video = models.FileField(upload_to='visitas/3/video/%Y/%m/%d/', verbose_name="Video de entrega de trabajos oficial al plantel y su correcto funcionamiento")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	si = models.ForeignKey(User, related_name="si_entrega_bebedero", null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Entregas de bebedero'