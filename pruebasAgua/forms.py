from django import forms
from .models import *

class PrimerPruebaCreateForm(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('reporte_toma_agua', 'video')
#		fields = ()

class PrimerPruebaUpdateForm1(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('resultados_laboratorio',)
#		fields = ()

class PrimerPruebaUpdateForm2(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('resultados_inifed', 'sugerencias_sp')
#		fields = ()

class PrimerPruebaUpdateForm3(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('dictamen_sistema_potabilizador', 'aprobacion')
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