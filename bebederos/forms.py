from django import forms
from .models import *
from accounts.models import Perfil

class BebederoCreateForm(forms.ModelForm):	
	class Meta:
		model = SistemaBebedero
		fields = ('mueble', 'ejecutora')

class BebederoEditForm(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ('sistema_de_potabilizacion', 'identificador_sp', 'secuencia_sp', 'modulo', 'linea_ensamblaje')

class BebederoGeneraNSForm(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ()		