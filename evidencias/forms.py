from django import forms
from .models import *

class EvidenciaPreviaCreateForm(forms.ModelForm):
	class Meta:
		model = EvidenciaPrevia
		fields = ('nombre', 'archivo', 'foto', 'video')

class EvidenciaInstalacionCreateForm(forms.ModelForm):
	class Meta:
		model = EvidenciaInstalacion
		fields = ('nombre', 'archivo', 'foto', 'video')

class EvidenciaPostInstalacionCreateForm(forms.ModelForm):
	class Meta:
		model = EvidenciaPostInstalacion
		fields = ('nombre', 'archivo', 'foto', 'video')	