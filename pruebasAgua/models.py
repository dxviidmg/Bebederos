from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from bebederos.models import *

class PrimerPrueba(models.Model):
	validacion_choices = (
		("Validado", "Validado"),
		("No validado", "No validado"),
		("En espera", "En espera"),
	)

	comparacion_choices = (
		("=", "="),
		("<", "<"),
		("≥", "≥"),
		("≤", "≤"),
	)

	modalidad_envio_choices = (
		("Paqueteria", "Paqueteria"),
		("Camión", "Camión"),
	)

	escuela = models.OneToOneField(User, related_name="escuela_primer_prueba")
	creacion = models.DateField(default=timezone.now, verbose_name="Fecha de creación")

	#Fase de Toma de Agua / SI
	reporte_toma_agua = models.FileField(upload_to='pruebas/1/reportes/%Y/%m/%d/', verbose_name="Etiqueta de muestra")
	foto_toma_agua_1 = models.FileField(upload_to='pruebas/1/fotos/%Y/%m/%d/', verbose_name="Fotografía de fachada de la escuela donde se muestre el CCT", null=True, blank=True)
	foto_toma_agua_2 = models.FileField(upload_to='pruebas/1/fotos/%Y/%m/%d/', verbose_name="Fotografía de muestra en el punto de muestreo", null=True, blank=True)

	#Fase de analisis / LAB
	resultados_laboratorio = models.FileField(upload_to='pruebas/1/resultados/%Y/%m/%d/', verbose_name="Resultados de análisis de laboratorio", null=True, blank=True)
	registro_campo = models.FileField(upload_to='pruebas/1/hojasCampo/%Y/%m/%d/', verbose_name="Registro de campo", null=True, blank=True)
	cadena_custodia = models.FileField(upload_to='pruebas/1/cadenasCustioda/%Y/%m/%d/', verbose_name="Cadena de custodia", null=True, blank=True)
#	modalidad_envio = models.CharField(max_length=11, choices=modalidad_envio_choices, verbose_name="Modalidad de envío", null=True, blank=True)
#	empresa_envio = models.CharField(max_length=20, verbose_name="Empresa de envío" , null=True, blank=True)
#	no_rastreabilidad = models.CharField(max_length=50, verbose_name="No. de rastreabilidad", null=True, blank=True)

	#Fase de confirmación / ECA
	validacion = models.CharField(max_length=11, default="En espera", choices=validacion_choices, verbose_name="Validación")
		
	#Información del analísis
	no_registro = models.CharField(max_length=30, null=True, blank=True, verbose_name="Número de registro (Orden de Trabajo)")
	creacion_reporte_analisis = models.DateField(null=True, blank=True, verbose_name="Fecha del reporte de análisis")

	#Comparaciones
	comparacion_color_verdadero = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_turbiedad = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_ph = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_conductividad_electrica = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_coliformes_fecales = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_coliformes_totales  = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_arsenico = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_hierro = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_manganeso  = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_plomo = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_floururos = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_nitratos = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_sulfatos = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_dureza_total = models.CharField(max_length=1, choices=comparacion_choices, default="=",verbose_name=".")
	comparacion_solidos_disueltos = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")

	#Parametros
		#Fisicos y organoelectricos
	color_verdadero = models.FloatField(null=True, blank=True, verbose_name="Color verdadero (U Pt-Co)")
	turbiedad = models.FloatField(null=True, blank=True, verbose_name="Turbiedad (UTN o equivalente)")
	ph = models.FloatField(null=True, blank=True, verbose_name="pH (unidades de pH)")
	conductividad_electrica = models.FloatField(null=True, blank=True, verbose_name="Conductividad eléctrica (µS/cm)")
		#Bacteriologicos
	coliformes_fecales = models.FloatField(null=True, blank=True, verbose_name="Coliformes fecales (UFC o NMP)")
	coliformes_totales = models.FloatField(null=True, blank=True, verbose_name="Coliformes totales (UFC o NMP)") 
		#Arsenico y metales
	arsenico = models.FloatField(null=True, blank=True, verbose_name="Arsénico (mg/L)")
	hierro = models.FloatField(null=True, blank=True, verbose_name="Hierro (mg/L)")
	manganeso = models.FloatField(null=True, blank=True, verbose_name="Manganeso (mg/L)")
	plomo = models.FloatField(null=True, blank=True, verbose_name="Plomo (mg/L)")
		#Iones y compuestos inorganicos
	floururos = models.FloatField(null=True, blank=True, verbose_name="Fluoruros (mg/L)")
	nitratos = models.FloatField(null=True, blank=True, verbose_name="Nitratos (mg/L)")
	sulfatos = models.FloatField(null=True, blank=True, verbose_name="Sulfatos (mg/L)")
	dureza_total = models.FloatField(null=True, blank=True, verbose_name="Dureza total (CaCO3) (mg/L)")
	solidos_disueltos  = models.FloatField(null=True, blank=True, verbose_name="Sólidos disueltos totales (mg/L)")

	def DeleteSB(self):
		if self.validacion == "No validado":
			SistemaBebedero.objects.get(escuela=self.escuela).delete()

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Primeras pruebas'

class SegundaPrueba(models.Model):
	validacion_choices = (
		("Validado", "Validado"),
		("No validado", "No validado"),
		("En espera", "En espera"),
	)
	comparacion_choices = (
		("=", "="),
		("<", "<"),
		("≥", "≥"),
		("≤", "≤"),		
	)

	modalidad_envio_choices = (
		("Paqueteria", "Paqueteria"),
		("Camión", "Camión"),
	)
		
	escuela = models.OneToOneField(User, related_name="escuela_segunda_prueba")	

	#Fase de Toma de Agua / SI
	reporte_toma_agua = models.FileField(upload_to='pruebas/2/reportes_de_toma/%Y/%m/%d/', verbose_name="Etiqueta de muestra")
	foto_toma_agua_1 = models.FileField(upload_to='pruebas/1/fotos/%Y/%m/%d/', verbose_name="Fotografía de fachada de la escuela donde se muestre el CCT", null=True, blank=True)
	foto_toma_agua_2 = models.FileField(upload_to='pruebas/1/fotos/%Y/%m/%d/', verbose_name="Fotografía de muestra en el punto de muestro", null=True, blank=True)

	#Fase de analisis / LAB
	registro_campo = models.FileField(upload_to='pruebas/1/hojasCampo/%Y/%m/%d/', verbose_name="Registro de campo", null=True, blank=True)
	cadena_custodia = models.FileField(upload_to='pruebas/1/cadenasCustioda/%Y/%m/%d/', verbose_name="Cadena de custodia", null=True, blank=True)
#	modalidad_envio = models.CharField(max_length=11, choices=modalidad_envio_choices, verbose_name="Modalidad de envío", null=True, blank=True)
#	empresa_envio = models.CharField(max_length=20, verbose_name="Empresa de envío" , null=True, blank=True)
#	no_rastreabilidad = models.CharField(max_length=50, verbose_name="No. de rastreabilidad", null=True, blank=True)

	#Fase de Sugerencias / ECA(Pilar)
	resultados_laboratorio = models.FileField(upload_to='pruebas/2/resultados/%Y/%m/%d/', verbose_name="Resultados de análisis de laboratorio", null=True, blank=True)

	#Fase de confirmación de IMTA
	dictamen_validacion = models.FileField(upload_to='pruebas/2/dictamenes/%Y/%m/%d/', verbose_name="Dictamen de validación", null=True, blank=True)
	validacion = models.CharField(max_length=11, default="En espera", choices=validacion_choices, verbose_name="Validación")

	creacion = models.DateField(default=timezone.now, verbose_name="Fecha de creación")

	#Datos de análisis
	no_registro = models.CharField(max_length=30, null=True, blank=True, verbose_name="Número de registro")	
	creacion_reporte_analisis = models.DateField(null=True, verbose_name="Fecha de creación del reporte de análisis")

	#Comparaciones
	comparacion_color_verdadero = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_turbiedad = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_ph = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_conductividad_electrica = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_coliformes_fecales = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_coliformes_totales  = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_arsenico = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_hierro = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_manganeso  = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_plomo = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_floururos = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_nitratos = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_sulfatos = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")
	comparacion_dureza_total = models.CharField(max_length=1, choices=comparacion_choices, default="=",verbose_name=".")
	comparacion_solidos_disueltos = models.CharField(max_length=1, choices=comparacion_choices, default="=", verbose_name=".")

	#Parámetros
		#Fisicos y organoelectricos
	color_verdadero = models.FloatField(null=True, blank=True, verbose_name="Color verdadero (U Pt-Co)")
	turbiedad = models.FloatField(null=True, blank=True, verbose_name="Turbiedad (UTN o equivalente)")
	ph = models.FloatField(null=True, blank=True, verbose_name="pH (unidades de pH)")
	conductividad_electrica = models.FloatField(null=True, blank=True, verbose_name="Conductividad eléctrica (µS/cm)")
		#Bacteriologicos
	coliformes_fecales = models.FloatField(null=True, blank=True, verbose_name="Coliformes fecales (UFC o NMP)")
	coliformes_totales = models.FloatField(null=True, blank=True, verbose_name="Coliformes totales (UFC o NMP)") 
		#Arsenico y metales
	arsenico = models.FloatField(null=True, blank=True, verbose_name="Arsénico (mg/L)")
	hierro = models.FloatField(null=True, blank=True, verbose_name="Hierro (mg/L)")
	manganeso = models.FloatField(null=True, blank=True, verbose_name="Manganeso (mg/L)")
	plomo = models.FloatField(null=True, blank=True, verbose_name="Plomo (mg/L)")
		#Iones y compuestos inorgánicos
	floururos = models.FloatField(null=True, blank=True, verbose_name="Fluoruros (mg/L)")
	nitratos = models.FloatField(null=True, blank=True, verbose_name="Nitratos (mg/L)")
	sulfatos = models.FloatField(null=True, blank=True, verbose_name="Sulfatos (mg/L)")
	dureza_total = models.FloatField(null=True, blank=True, verbose_name="Dureza total (CaCO3) (mg/L)")
	solidos_disueltos  = models.FloatField(null=True, blank=True, verbose_name="Sólidos disueltos totales (mg/L)")

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Segundas pruebas'