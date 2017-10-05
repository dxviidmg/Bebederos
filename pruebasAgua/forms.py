from django import forms
from .models import *

class PrimerPruebaCreateForm(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('reporte_toma_agua', 'foto_toma_agua')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(PrimerPruebaCreateForm, self).__init__(*args, **kwargs)
		self.fields['reporte_toma_agua'].required = True
		self.fields['foto_toma_agua'].required = True

class PrimerPruebaUpdateForm1(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('resultados_laboratorio', 'foto_recepcion',)
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm1, self).__init__(*args, **kwargs)
		self.fields['resultados_laboratorio'].required = True
		self.fields['foto_recepcion'].required = True

class PrimerPruebaUpdateForm2(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('resultados_IMTA',)
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm2, self).__init__(*args, **kwargs)
		self.fields['resultados_IMTA'].required = True

class PrimerPruebaUpdateForm3(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('dictamen_sistema_potabilizador', 'aprobacion')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm3, self).__init__(*args, **kwargs)
		self.fields['dictamen_sistema_potabilizador'].required = True

"""Segunda Prueba de Calidad de Agua"""
class SegundaPruebaCreateForm(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('reporte_toma_agua',	'foto_toma_agua',)
#		fields = ()

class SegundaPruebaUpdateForm1(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('resultados_laboratorio', 'foto_recepcion')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm1, self).__init__(*args, **kwargs)
		self.fields['resultados_laboratorio'].required = True
		self.fields['foto_recepcion'].required = True

class SegundaPruebaUpdateForm2(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('resultados_IMTA', 'aprobacion_interna')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm2, self).__init__(*args, **kwargs)
		self.fields['resultados_IMTA'].required = True
		self.fields['aprobacion_interna'].required = True

class SegundaPruebaUpdateForm3(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('dictamen_validacion', 'aprobacion')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm3, self).__init__(*args, **kwargs)
		self.fields['dictamen_validacion'].required = True
		self.fields['aprobacion'].required = True	