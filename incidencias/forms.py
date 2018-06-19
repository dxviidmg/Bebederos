from django import forms
from .models import *

class IncidenciaCreateForm(forms.ModelForm):
	class Meta:
		model = Incidencia
		fields = ('fase', 'prioridad', 'descripcion', 'evidencia')

class IncidenciaEditForm(forms.ModelForm):
	class Meta:
		model = Incidencia
		fields = ('solucion', 'status', 'evidencia_2')		