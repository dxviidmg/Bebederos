from django import forms
from .models import *
from accounts.models import Perfil

class BebederoCreateForm(forms.ModelForm):	
	class Meta:
		model = SistemaBebedero
		fields = ('mueble', 'sistema_de_potabilizacion', 'identificador_sp', 'qr_sp', 'modulo', 'ejecutora', 'linea_ensamblaje')

class BebederoEditForm(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ('mueble', 'sistema_de_potabilizacion', 'identificador_sp', 'qr_sp', 'modulo', 'ejecutora', 'linea_ensamblaje')

class BebederoGeneraNSForm(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ()		