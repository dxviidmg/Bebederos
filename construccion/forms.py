from django import forms
from .models import *

class InicioDeTrabajoCreateForm(forms.ModelForm):
	class Meta:
		model = InicioDeTrabajo
		fields = ('acta_inicio',)

class EnvolventeTerminadaCreateForm(forms.ModelForm):
	class Meta:
		model = EnvolventeTerminada
		fields = ('video',)
#		fields = ()

class EvidenciaConstruccionCreateForm(forms.ModelForm):
	class Meta:
		model = EvidenciaConstruccion
		fields = ('fase', 'foto')

class EvidenciaConstruccionEditForm(forms.ModelForm):
	class Meta:
		model = EvidenciaConstruccion
		fields = ('aprobacion_SI',)