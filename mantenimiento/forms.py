from django import forms
from .models import *

class MantenimientoCreateForm(forms.ModelForm):
	class Meta:
		model = Mantenimiento
		fields = ('mes', 'año', 'carnet', 'tipo', 'descripcion', 'volumen')

	def __init__(self, user, **kwargs):
		super(MantenimientoCreateForm, self).__init__(**kwargs)
		if user.perfil.tipo == "INIFED" or user.perfil.tipo == "CEstatal":
			print("Reconoce que es un funcionario de INIFED")
#			self.fields['tipo'] = [('Preven' , 'Preven'),('Correc' , 'Correc')]