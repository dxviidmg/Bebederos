from django import forms
from .models import *
from accounts.models import Perfil

class BebederoCreateForm(forms.ModelForm):	
	class Meta:
		model = SistemaBebedero
		fields = ('mueble', 'ejecutora')

	def __init__(self, *args, **kwargs):
		super(BebederoCreateForm, self).__init__(**kwargs)
		perfilesEjecutoras = Perfil.objects.filter(tipo="Ejecutora")
		self.fields['ejecutora'].queryset = User.objects.filter(perfil__in=perfilesEjecutoras)

#ECA
class BebederoEditForm1(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ('sistema_potabilizacion', 'identificador_sp', 'componentes_sp',)
	def __init__(self, *args, **kwargs):
		super(BebederoEditForm1, self).__init__(*args, **kwargs)
		self.fields['sistema_potabilizacion'].required = True
		self.fields['identificador_sp'].required = True
		self.fields['componentes_sp'].required = True
#Taller
class BebederoEditForm2(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ('linea_ensamblaje',)
	def __init__(self, *args, **kwargs):
		super(BebederoEditForm2, self).__init__(*args, **kwargs)
		self.fields['linea_ensamblaje'].required = True

class BebederoEditForm3(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ('asignacion',)
#	def __init__(self, *args, **kwargs):
#		super(BebederoEditForm2, self).__init__(*args, **kwargs)
#		self.fields['linea_ensamblaje'].required = True		