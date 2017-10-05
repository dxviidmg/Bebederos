from django import forms
from .models import *

class EscuelaUserCreateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name',)

		labels = {
			"username": "C. C. T."
		}

class EscuelaPerfilCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('nivel_educativo', 'plantilla_escolar', 'domicilio', 'localidad')

class EscuelaUserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email',)

class EscuelaPerfilUpdateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('turno', 'foto_escuela', 'telefono', 'director', 'foto_director', 'conexion', 'referencias', 'SSID', 'clave_SSID')