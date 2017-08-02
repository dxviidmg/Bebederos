from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class InicioDeTrabajo(models.Model):
	escuela = models.OneToOneField(User)
	acta_inicio = models.FileField(upload_to='trabajos/inicio/acta/%Y/%m/%d/', verbose_name="Acta de inicios de trabajos")
	hoja_cotizacion = models.FileField(upload_to='visitas/1/cotizacion/%Y/%m/%d/', verbose_name="Hoja de cotizaciones")
	sim = models.ForeignKey(User, related_name="sim_inicio_trabajo", null=True, blank=True)

	def __str__(self):
		return '{} para escuela'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Inicio de trabajos'

class InstalacionBebedero(models.Model):
	escuela = models.OneToOneField(User)
	reporte = models.FileField(upload_to='instalaciones/reporte/%Y/%m/%d/', verbose_name="Reporte de instalación")
	plantilla_fotografica = models.FileField(upload_to='instalaciones/plantilla/%Y/%m/%d/', verbose_name="Plantilla fotográfica de su instalación y funcionamiento")
	recepcion_mueble_bebedero = models.FileField(upload_to='instalaciones/recepcion/%Y/%m/%d/', verbose_name="Recepción del mueble bebedero y sus componentes")
	sim = models.ForeignKey(User, related_name="sim_instalacion_sb",)

	def __str__(self):
		return '{} para escuela'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Instalaciones de Sistemas bebedero'

class TerminoDeTrabajo(models.Model):
	escuela = models.OneToOneField(User)
	reporte_segunda_toma = models.FileField(upload_to='visitas/2/reporte_de_toma/%Y/%m/%d/', verbose_name="Reporte de segunda toma de muestra")
	plantilla_fotografica = models.FileField(upload_to='instalaciones/plantilla/%Y/%m/%d/', verbose_name="Plantilla fotográfica de su instalación y funcionamiento")
	sim = models.ForeignKey(User, related_name="sim_termino_trabajo", null=True, blank=True)

	def __str__(self):
		return '{} para escuela'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Terminos de trabajo'