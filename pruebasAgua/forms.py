from django import forms
from .models import *

class PrimerPruebaCreateForm(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('reporte_toma_agua', 'dictamen_validacion', 'constancia_recepcion',	'video', 'resultados', 'dictamen_sistema_potabilizador',)
#		fields = ()

class PrimerPruebaEditForm(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('aprobacion',)
#		fields = ()

class SegundaPruebaCreateForm(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('reporte_toma_agua', 'dictamen_validacion', 'constancia_recepcion',	'video', 'resultados',)
#		fields = ()

class SegundaPruebaEditForm(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('aprobacion',)
#		fields = ()