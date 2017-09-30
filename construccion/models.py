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
	plano_instalacion = models.FileField(upload_to='instalaciones/planos/%Y/%m/%d/', verbose_name="Plano de Instalaciones")
	memoria_calculo = models.FileField(upload_to='instalaciones/memorias/%Y/%m/%d/', verbose_name="Memorias de cálculo")
	trabajos_de_conexion = models.FileField(upload_to='instalaciones/memorias/%Y/%m/%d/', verbose_name="Trabajos de conexión")
	recepcion_mueble_bebedero = models.FileField(upload_to='instalaciones/recepcion/%Y/%m/%d/', verbose_name="Recepción del mueble bebedero y sus componentes")
	si = models.ForeignKey(User, related_name="sim_instalacion_sb", verbose_name="Superintendente")

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Instalaciones de Sistemas Bebedero'

class TerminoDeTrabajo(models.Model):
	escuela = models.OneToOneField(User)
	acta_termino = models.FileField(upload_to='trabajos/inicio/acta/%Y/%m/%d/', verbose_name="Acta de termino de trabajo", default="default.pdf")
	video = models.FileField(upload_to='instalaciones/plantilla/%Y/%m/%d/', verbose_name="Evidencia audiovisual", default="default.pdf")
	si = models.ForeignKey(User, related_name="sim_termino_trabajo", null=True, blank=True, verbose_name="Superintendente",)

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Terminos de trabajo'

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
	ejecutora = models.ForeignKey(User, related_name="ejecutora_bitacora")
	aprobacion_SI = models.CharField(max_length=11, default="En espera", choices=aprobacion_choices, verbose_name="Aprobación de SI")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")

	def __str__(self):
		return 'Fase {} de {}'.format(self.fase, self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Evidencias de construcción'

class NotaDeBitacora(models.Model):
	prioridad_choices = (
		("Alta", "Alta"),
		("Media", "Media"),
		("Baja", "Baja"),
	)
	escuela = models.ForeignKey(User)
	nota = models.TextField()
	autor = models.ForeignKey(User, related_name="autor_nota")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	prioridad = models.CharField(max_length=5, choices=prioridad_choices)
	resuelto = models.BooleanField(default=False)

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Notas de bitacora'