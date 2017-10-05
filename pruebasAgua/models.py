from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class PrimerPrueba(models.Model):
	aprobacion_choices = (
		("En espera", "En espera"),
		("Aprobado", "Aprobado"),
		("No aprobado", "No aprobado"),
	)
	escuela = models.OneToOneField(User)

	#Fase de Toma de Agua / SI
	reporte_toma_agua = models.FileField(upload_to='pruebas/1/reporte_de_toma/%Y/%m/%d/', verbose_name="Reporte de toma de muestra")
	foto_toma_agua = models.FileField(upload_to='pruebas/1/fotos/%Y/%m/%d/', verbose_name="Evidencia fotográfica de toma de agua")

	#Fase de analisis / LAB
	resultados_laboratorio = models.FileField(upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name="Resultados de análisis de laboratorio", null=True, blank=True)
	foto_recepcion = models.FileField(upload_to='pruebas/1/fotos/%Y/%m/%d/', verbose_name="Evidencia fotográfica de recepción de muestra", null=True, blank=True)

	#Fase de Sugerencias / ECA(Pilar)
	resultados_IMTA = models.FileField(upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name="Resultados de análisis con propuesta de sistema potabilizador para visto bueno de IMTA", null=True, blank=True)

	#Fase de confirmación de IMTA
	dictamen_sistema_potabilizador = models.FileField(upload_to='pruebas/1/dictamen/%Y/%m/%d/', verbose_name="Dictamen del sistema potabilizador a utilizar", null=True, blank=True)
	aprobacion = models.CharField(max_length=11, default="En espera", choices=aprobacion_choices, verbose_name="Aprobación")

	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	laboratorio = models.ForeignKey(User, related_name="lab_primer_prueba")
	
	#Parametros
	color_verdadero = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Color verdadero (U Pt-Co)")
	turbiedad = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Turbiedad (UTN o equivalente)")
	ph = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="pH (unidades de pH)")
	conductividad_electrica = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Conductividad eléctrica (µS/cm)")
	coliformes_fecales = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Coliformes fecales (unidades)")
	coliformes_totales = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Coliformes totales (Unidades)") 
	arsenico = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Arsénico")
	hierro = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Hierro")
	manganesio = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Manganeso")
	plomo = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Plomo")
	floururos = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Fluoruros")
	nitratos = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Nitratos")
	sulfatos = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Sulfatos")
	dureza_total = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Dureza total (CaCO3)")
	solidos_disueltos  = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Sólidos disueltos totales")

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Primeras pruebas'

class SegundaPrueba(models.Model):
	aprobacion_choices = (
		("En espera", "En espera"),
		("Aprobado", "Aprobado"),
		("No aprobado", "No aprobado"),
	)
	escuela = models.OneToOneField(User)

	#Fase de Toma de Agua / SI
	reporte_toma_agua = models.FileField(upload_to='pruebas/2/reporte_de_toma/%Y/%m/%d/', verbose_name="Reporte de toma de muestra")
	foto_toma_agua = models.FileField(upload_to='pruebas/2/video/%Y/%m/%d/', verbose_name="Evidencia fotográfica de toma de agua")

	#Fase de analisis / LAB
	resultados_laboratorio = models.FileField(upload_to='pruebas/2/resultados/%Y/%m/%d/', verbose_name="Resultados de análisis de laboratorio", null=True, blank=True)
	foto_recepcion = models.FileField(upload_to='pruebas/2/fotos/%Y/%m/%d/', verbose_name="Evidencia fotografica de recepción de muestra", null=True, blank=True)

	#Fase de Sugerencias / ECA(Pilar)
	resultados_IMTA = models.FileField(upload_to='pruebas/2/resultados/%Y/%m/%d/', verbose_name="Resultados de análisis para IMTA", null=True, blank=True)
	aprobacion_interna = models.FileField(upload_to='pruebas/2/resultados/%Y/%m/%d/', null=True, blank=True, verbose_name="Aprobación interna")

	#Fase de confirmación de IMTA
	dictamen_validacion = models.FileField(upload_to='pruebas/2/resultados/%Y/%m/%d/', verbose_name="Dictamen de validación", null=True, blank=True)
	aprobacion = models.CharField(max_length=11, default="En espera", choices=aprobacion_choices, verbose_name="Aprobación")

	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	laboratorio = models.ForeignKey(User, related_name="lab_segunda_prueba")

	#Parametros

	#Parametros
	color_verdadero = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Color verdadero (U Pt-Co)")
	turbiedad = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Turbiedad (UTN o equivalente)")
	ph = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="pH (unidades de pH)")
	conductividad_electrica = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Conductividad eléctrica (µS/cm)")
	coliformes_fecales = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Coliformes fecales (unidades)")
	coliformes_totales = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Coliformes totales (Unidades)") 
	arsenico = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Arsénico")
	hierro = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Hierro")
	manganesio = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Manganeso")
	plomo = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Plomo")
	floururos = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Fluoruros")
	nitratos = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Nitratos")
	sulfatos = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Sulfatos")
	dureza_total = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Dureza total (CaCO3)")
	solidos_disueltos  = models.DecimalField(max_digits=7, decimal_places=3, null=True, blank=True, verbose_name="Sólidos disueltos totales")

	
	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Segundas pruebas'