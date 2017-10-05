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
		fields = ('sistema_de_potabilizacion', 'identificador_sp', 'componentes_sp', 'linea_ensamblaje')

class BebederoGeneraNSForm(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ()		