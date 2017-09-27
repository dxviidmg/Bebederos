from django import forms
from .models import *
from accounts.models import Perfil

class BebederoCreateForm(forms.ModelForm):	
	class Meta:
		model = SistemaBebedero
		fields = ('identificador_mb', 'mueble', 'sistema_de_potabilizacion', 'identificador_sp', 'qr_sp', 'modulo', 'ejecutora')

class BebederoEditForm(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ('identificador_mb', 'mueble', 'sistema_de_potabilizacion', 'identificador_sp', 'qr_sp', 'modulo', 'ejecutora')	