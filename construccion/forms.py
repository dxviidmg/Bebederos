from django import forms
from .models import *

class InicioDeTrabajoCreateForm(forms.ModelForm):
	class Meta:
		model = InicioDeTrabajo
		fields = ('acta_inicio',)

class InstalacionBebederoCreateForm(forms.ModelForm):
	class Meta:
		model = InstalacionBebedero
		fields = ('reporte', 'plano_instalacion', 'memoria_calculo', 'trabajos_de_conexion', 'recepcion_mueble_bebedero')
#		fields = ()

class TerminoDeTrabajoCreateForm(forms.ModelForm):
	class Meta:
		model = TerminoDeTrabajo
		fields = ('reporte_segunda_toma', 'plantilla_fotografica')

class EvidenciaConstruccionCreateForm(forms.ModelForm):
	class Meta:
		model = EvidenciaConstruccion
		fields = ('fase', 'video')

class NotaDeBitacoraCreateForm(forms.ModelForm):
	class Meta:
		model = NotaDeBitacora
		fields = ('nota', 'prioridad')