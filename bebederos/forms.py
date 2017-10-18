from django import forms
from .models import *
from accounts.models import Perfil

class BebederoCreateForm(forms.ModelForm):	
	class Meta:
		model = SistemaBebedero
		fields = ('mueble',)

#	def __init__(self, *args, **kwargs):
#		super(BebederoCreateForm, self).__init__(**kwargs)
#		perfilesEjecutoras = Perfil.objects.filter(tipo="Ejecutora")
#		self.fields['ejecutora'].queryset = User.objects.filter(perfil__in=perfilesEjecutoras)

#ECA
class BebederoUpdateForm1(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ('sistema_potabilizacion', 'identificador_sp', 'etapas_sp',)
	def __init__(self, *args, **kwargs):
		super(BebederoUpdateForm1, self).__init__(*args, **kwargs)
		self.fields['sistema_potabilizacion'].required = True
		self.fields['identificador_sp'].required = True
		self.fields['etapas_sp'].required = True
#Taller
class BebederoUpdateForm2(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ('linea_ensamblaje',)
	def __init__(self, *args, **kwargs):
		super(BebederoUpdateForm2, self).__init__(*args, **kwargs)
		self.fields['linea_ensamblaje'].required = True

class BebederoUpdateForm3(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ('asignacion',)
#	def __init__(self, *args, **kwargs):
#		super(BebederoEditForm2, self).__init__(*args, **kwargs)
#		self.fields['linea_ensamblaje'].required = True

class BebederoUpdateForm4(forms.ModelForm):	
	class Meta:
		model = SistemaBebedero
		fields = ('ejecutora',)

	def __init__(self, *args, **kwargs):
		super(BebederoUpdateForm4, self).__init__(**kwargs)
		perfilesEjecutoras = Perfil.objects.filter(tipo="Ejecutora")
		self.fields['ejecutora'].queryset = User.objects.filter(perfil__in=perfilesEjecutoras)