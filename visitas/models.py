from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class VisitaDeAcuerdo(models.Model):
	escuela = models.OneToOneField(User, related_name="escuela_visita_acuerdo")
	acta_ubicacion = models.FileField(upload_to='visita/actas/%Y/%m/%d/', verbose_name="Acta de ubicación de bebedero", null=True, blank=True)
	cedula_identificacion = models.FileField(upload_to='visita/cedulas/%Y/%m/%d/', verbose_name="Cédula de identificación", null=True, blank=True)
	convenio_concertacion = models.FileField(upload_to='visitas/concertaciones/%Y/%m/%d/', verbose_name="Convenio de concertación de aplicación de recurso", null=True, blank=True)
	constancia_integracion_comite = models.FileField(upload_to='visitas/comites/%Y/%m/%d/', verbose_name="Constancia de integración de comité", null=True, blank=True)
	plano_conjunto = models.FileField(upload_to='visitas/planosConjunto/%Y/%m/%d/', verbose_name="Plano de conjunto", null=True, blank=True)
	distribucion_planta = models.FileField(upload_to='visitas/distribuciones/%Y/%m/%d/', verbose_name="Distribución en planta", null=True, blank=True)	
	memoria_calculo_1 = models.FileField(upload_to='instalaciones/memorias/%Y/%m/%d/', verbose_name="Memoria de cálculo hidráulico", null=True, blank=True)
	memoria_calculo_2 = models.FileField(upload_to='instalaciones/memorias/%Y/%m/%d/', verbose_name="Memoria de cálculo sanitario", null=True, blank=True)
	memoria_calculo_3 = models.FileField(upload_to='instalaciones/memorias/%Y/%m/%d/', verbose_name="Memoria de cálculo eléctrico", null=True, blank=True)		
	isometrico_instalacion = models.FileField(upload_to='visitas/pihs/%Y/%m/%d/', verbose_name="Isometricos de instalaciones", null=True, blank=True)
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Visitas de acuerdo'

class InicioFuncionamiento(models.Model):
	escuela = models.OneToOneField(User, related_name="escuela_inicio_funcionamiento")
	acta_funcionamiento = models.FileField(upload_to='funcionamiento/actas/%Y/%m/%d/', verbose_name="Acta",  null=True, blank=True)
	recibo_llaves = models.FileField(upload_to='funcionamiento/recibos/%Y/%m/%d/', verbose_name="Recibo de llaves", null=True, blank=True)
	foto = models.FileField(upload_to='funcionamiento/fotos/%Y/%m/%d/', verbose_name="Evidencia fotográfica 1", null=True, blank=True)
	foto_2 = models.FileField(upload_to='funcionamiento/fotos/%Y/%m/%d/', verbose_name="Evidencia fotográfica 2", null=True, blank=True)
	foto_3 = models.FileField(upload_to='funcionamiento/fotos/%Y/%m/%d/', verbose_name="Evidencia fotográfica 3", null=True, blank=True)	
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Inicios de funcionamiento'

class ActaEntrega(models.Model):
	escuela = models.OneToOneField(User, related_name="escuela_acta_entrega")
	acta_entrega = models.FileField(upload_to='entrega/actas/%Y/%m/%d/', verbose_name="Acta de entrega")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	
	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Actas de entrega'