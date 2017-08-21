from django import forms
from .models import *

class InicioDeTrabajoCreateForm(forms.ModelForm):
	class Meta:
		model = InicioDeTrabajo
		fields = ('acta_inicio',)

class InicioDeTrabajoEditForm(forms.ModelForm):
	class Meta:
		model = InicioDeTrabajo
		fields = ('acta_inicio',)

class InstalacionBebederoCreateForm(forms.ModelForm):
	class Meta:
		model = InstalacionBebedero
		#fields = ('reporte', 'plantilla_fotografica', 'recepcion_mueble_bebedero')
		fields = ()

class InstalacionBebederoEditForm(forms.ModelForm):
	class Meta:
		model = InstalacionBebedero
		#fields = ('reporte', 'plantilla_fotografica', 'recepcion_mueble_bebedero')
		fields = ()

class TerminoDeTrabajoCreateForm(forms.ModelForm):
	class Meta:
		model = TerminoDeTrabajo
		fields = ('reporte_segunda_toma', 'plantilla_fotografica')

class TerminoDeTrabajoEditForm(forms.ModelForm):
	class Meta:
		model = TerminoDeTrabajo
		fields = ('reporte_segunda_toma', 'plantilla_fotografica')

class EvidenciaConstruccionCreateForm(forms.ModelForm):
	class Meta:
		model = EvidenciaConstruccion
		fields = ('fase', 'video')		