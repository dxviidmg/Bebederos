from django import forms
from .models import *

class PrimerPruebaCreateForm(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('constancia_recepcion', 'video', 'resultados',)