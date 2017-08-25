from django import forms
from .models import *

class IncidenciaCreateForm(forms.ModelForm):
	class Meta:
		model = Incidencia
		fields = ('etapa', 'prioridad', 'descripcion')	