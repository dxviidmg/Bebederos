from django import forms
from .models import *

class BebederoCreateOrEditForm(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ('identificador_mb', 'mueble', 'sistema_de_potabilizacion', 'identificador_sp', 'qr_sp', 'modulo')