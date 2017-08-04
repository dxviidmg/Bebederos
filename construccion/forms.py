from django import forms
from .models import *

class InicioDeTrabajoCreateForm(forms.ModelForm):
	class Meta:
		model = InicioDeTrabajo
		fields = ('acta_inicio', 'hoja_cotizacion')

class InicioDeTrabajoEditForm(forms.ModelForm):
	class Meta:
		model = InicioDeTrabajo
		fields = ('acta_inicio', 'hoja_cotizacion')

class InstalacionBebederoCreateForm(forms.ModelForm):
	class Meta:
		model = InstalacionBebedero
		fields = ('reporte', 'plantilla_fotografica', 'recepcion_mueble_bebedero')

class InstalacionBebederoEditForm(forms.ModelForm):
	class Meta:
		model = InstalacionBebedero
		fields = ('reporte', 'plantilla_fotografica', 'recepcion_mueble_bebedero')

class TerminoDeTrabajoCreateForm(forms.ModelForm):
	class Meta:
		model = TerminoDeTrabajo
		fields = ('reporte_segunda_toma', 'plantilla_fotografica')