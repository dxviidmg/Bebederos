from django import forms
from .models import *

class EscuelaUserCreateForm(forms.ModelForm):
	class Meta:
		model = User

		fields = ('username', 'first_name',)

		labels = {
			"username": "C. C. T."
		}

		help_texts = {
			'username': None,
		}

	def clean_username(self):
	    username = self.cleaned_data['username']
	    try:
	        user = User.objects.exclude(pk=self.instance.pk).get(username=username)
	    except User.DoesNotExist:
	        return username
	    raise forms.ValidationError(u'Esta escuela "%s" ya ha sido registrada.' % username)

class EscuelaPerfilCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('nivel_educativo', 'plantilla_escolar', 'domicilio', 'localidad', 'coordenadas')
		
class EscuelaUserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email',)

class EscuelaPerfilUpdateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('turno', 'foto_escuela', 'telefono', 'director', 'foto_director', 'domicilio', 'referencias', 'SSID', 'clave_SSID', 'coordenadas')