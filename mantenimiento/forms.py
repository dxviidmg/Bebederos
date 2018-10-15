from django import forms
from .models import *

class MantenimientoCreateForm(forms.ModelForm):
	class Meta:
		model = Mantenimiento
		fields = ('mes', 'año', 'fecha', 'carnet', 'foto_1', 'foto_2', 'tipo', 'descripcion', 'volumen')