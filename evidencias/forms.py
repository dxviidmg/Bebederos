from django import forms
from .models import *

class EvidenciaCreateForm(forms.ModelForm):
	class Meta:
		model = Evidencia
		fields = ('nombre', 'archivo', 'foto', 'video')