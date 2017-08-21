from django import forms
from .models import *

class PrimerPruebaCreateForm(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('constancia_recepcion', 'video', 'resultados',)
#		fields = ()

class PrimerPruebaEditForm(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('aprobacion',)
#		fields = ()

class SegundaPruebaCreateForm(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('constancia_recepcion', 'video', 'resultados',)
#		fields = ()

class SegundaPruebaEditForm(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('aprobacion',)
#		fields = ()