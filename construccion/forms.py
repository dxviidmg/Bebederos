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