from django import forms
from .models import *

class IncidenciaCreateForm(forms.ModelForm):
	class Meta:
		model = Inciencia
		fields = ('etapa', 'prioridad', 'descripcion')	