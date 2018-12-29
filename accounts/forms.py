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
			print(username[0])
		raise forms.ValidationError(u'Esta escuela "%s" ya ha sido registrada.' % username)

class EscuelaPerfilCreateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('numero', 'localidad', 'domicilio', 'nivel_educativo', 'plantilla_escolar', 'coordenadas')
		
class EscuelaUserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email',)

class EscuelaPerfilUpdateForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('numero', 'director', 'turno', 'foto_escuela', 'telefono', 'domicilio', 'referencias', 'SSID', 'clave_SSID', 'coordenadas', 'expediente_tecnico')

class EntidadUpdateForm(forms.ModelForm):
	class Meta:
		model = Entidad
		fields = ('doc1', 'fecha_doc1', 'doc2', 'fecha_doc2', 'doc3', 'fecha_doc3')