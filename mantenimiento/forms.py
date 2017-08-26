from django import forms
from .models import *

class MantenimientoCreateForm(forms.ModelForm):
	class Meta:
		model = Mantenimiento
		fields = ('mes', 'año', 'carnet')