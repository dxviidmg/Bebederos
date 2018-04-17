from django import forms
from .models import *
from accounts.models import Perfil

class BebederoCreateForm(forms.ModelForm):	
	class Meta:
		model = SistemaBebedero
		fields = ('mueble',)

#PQ
class BebederoUpdateForm1(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ('sistema_potabilizacion', 'no_serie_sp',)
	def __init__(self, *args, **kwargs):
		super(BebederoUpdateForm1, self).__init__(*args, **kwargs)
		self.fields['sistema_potabilizacion'].required = True
		self.fields['no_serie_sp'].required = True

#PM
class BebederoUpdateForm2(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ('proveedor', 'no_serie_mueble')
	def __init__(self, *args, **kwargs):
		super(BebederoUpdateForm2, self).__init__(*args, **kwargs)
#		self.fields['linea_ensamblaje'].required = True

class BebederoUpdateForm3(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ('asignacion',)
#	def __init__(self, *args, **kwargs):
#		super(BebederoEditForm3, self).__init__(*args, **kwargs)
#		self.fields['asignacion'].required = True

#ECA
class BebederoUpdateForm5(forms.ModelForm):
	class Meta:
		model = SistemaBebedero
		fields = ('sistema_potabilizacion',)
	def __init__(self, *args, **kwargs):
		super(BebederoUpdateForm5, self).__init__(*args, **kwargs)
		self.fields['sistema_potabilizacion'].required = True