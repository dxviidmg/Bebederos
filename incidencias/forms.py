from django import forms
from .models import *

class IncidenciaCreateForm(forms.ModelForm):
	class Meta:
		model = Incidencia
		fields = ('fase', 'prioridad', 'descripcion')

class IncidenciaEditForm(forms.ModelForm):
	class Meta:
		model = Incidencia
		fields = ('solucion', 'status')		