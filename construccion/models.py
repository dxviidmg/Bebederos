from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class InicioDeTrabajo(models.Model):
	escuela = models.OneToOneField(User)
	acta_inicio = models.FileField(upload_to='trabajos/inicio/acta/%Y/%m/%d/', verbose_name="Acta de inicio de trabajo")
	si = models.ForeignKey(User, related_name="si_inicio_trabajo", null=True, blank=True, verbose_name="Superintendente")

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Inicio de trabajos'

class InstalacionBebedero(models.Model):
	escuela = models.OneToOneField(User)
	reporte = models.FileField(upload_to='instalaciones/reporte/%Y/%m/%d/', verbose_name="Reporte de instalación")
	trabajos_de_conexion = models.FileField(upload_to='instalaciones/memorias/%Y/%m/%d/', verbose_name="Trabajos de conexión")
	recepcion_mueble_bebedero = models.FileField(upload_to='instalaciones/recepcion/%Y/%m/%d/', verbose_name="Recepción del mueble bebedero y sus componentes")
	si = models.ForeignKey(User, related_name="sim_instalacion_sb", verbose_name="Superintendente")

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Instalaciones de Sistemas Bebedero'

class EvidenciaConstruccion(models.Model):
	fase_choices = (
		("Firme", "Firme"),
		("Muro", "Muro"),
		("Techumbre y puerta", "Techumbre y puerta"),
		("Instalación de Mueble Bebedero", "Instalación de Mueble Bebedero")
	)

	aprobacion_choices = (
		("En espera", "En espera"),
		("Aprobado", "Aprobado"),
		("No aprobado", "No aprobado"),
	)

	escuela = models.ForeignKey(User, related_name="escuela_evidencia")
	fase = models.CharField(max_length=30, choices=fase_choices)
	video = models.FileField(upload_to='instalaciones/bitacora/video/%Y/%m/%d/', verbose_name="Evidencia audio visual")
	aprobacion_SI = models.CharField(max_length=11, default="En espera", choices=aprobacion_choices, verbose_name="Aprobación de SI")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")

	def __str__(self):
		return 'Fase {} de {}'.format(self.fase, self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Evidencias de construcción'