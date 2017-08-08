from django import forms
from .models import *

class PrimerPruebaCreateForm(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('constancia_recepcion', 'video', 'resultados',)

class PrimerPruebaEditForm(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('aprobacion',)

class SegundaPruebaCreateForm(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('constancia_recepcion', 'video', 'resultados',)

class SegundaPruebaEditForm(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('aprobacion',)