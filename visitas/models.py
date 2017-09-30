from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class VisitaDeAcuerdo(models.Model):
	escuela = models.OneToOneField(User)
	#SI
	convenio_concertacion = models.FileField(upload_to='visitas/2/concertacion/%Y/%m/%d/', verbose_name="Convenio de concertación de aplicación de recurso")
	cedula_identificacion = models.FileField(upload_to='visitas/2/identificacion/%Y/%m/%d/', verbose_name="Cédula de identificación básica")
	acta_acuerdos = models.FileField(upload_to='visitas/2/acta/%Y/%m/%d/', verbose_name="Acta de acuerdos y ubicación del módulo")
	constancia_integracion_comite = models.FileField(upload_to='visitas/2/comite/%Y/%m/%d/', verbose_name="Constancia de Integración de Comité")
	#Ejecutora
	plano_instalacion_electrica = models.FileField(upload_to='visitas/2/acta/%Y/%m/%d/', verbose_name="Plano de instalación electrica", null=True, blank=True)
	plano_instalacion_hidraulica = models.FileField(upload_to='visitas/2/acta/%Y/%m/%d/', verbose_name="Plano de instalación hidraulica", null=True, blank=True)
	plano_instalacion_sanitaria = models.FileField(upload_to='visitas/2/acta/%Y/%m/%d/', verbose_name="Plano de instalación sanitaria", null=True, blank=True)
	estimacion = models.FileField(upload_to='visitas/2/acta/%Y/%m/%d/', verbose_name="Estimación", null=True, blank=True)

	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	si = models.ForeignKey(User, related_name="si_visita_acuerdo")

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Visitas de acuerdo'

class EntregaDeBebedero(models.Model):
	escuela = models.OneToOneField(User)
	acta_funcionamiento = models.FileField(upload_to='visitas/3/acta/%Y/%m/%d/', verbose_name="Acta de inicio de funcionamiento")
	convenio_responsabilidades = models.FileField(upload_to='visitas/3/responsabilidades/%Y/%m/%d/', verbose_name="Convenio de asignación de responsabilidades")
	video = models.FileField(upload_to='visitas/3/video/%Y/%m/%d/', verbose_name="Video de entrega de trabajos oficial al plantel y su correcto funcionamiento")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	si = models.ForeignKey(User, related_name="si_entrega_bebedero", null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Entregas de bebedero'