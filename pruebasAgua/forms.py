from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget

class PrimerPruebaCreateForm(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('reporte_toma_agua', 'foto_toma_agua_1', 'foto_toma_agua_2', 'video_toma_agua')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(PrimerPruebaCreateForm, self).__init__(*args, **kwargs)
		self.fields['reporte_toma_agua'].required = True
		self.fields['foto_toma_agua_1'].required = True
		self.fields['foto_toma_agua_2'].required = True
		self.fields['video_toma_agua'].required = True

class PrimerPruebaUpdateForm1(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('registro_campo', 'cadena_custodia')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm1, self).__init__(*args, **kwargs)
		self.fields['registro_campo'].required = True
		self.fields['cadena_custodia'].required = True

class PrimerPruebaUpdateForm2(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('no_registro', )
#		fields = ()

	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm2, self).__init__(*args, **kwargs)
		self.fields['no_registro'].required = True

class PrimerPruebaUpdateForm3(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('color_verdadero', 'turbiedad', 'ph', 'conductividad_electrica')

	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm3, self).__init__(*args, **kwargs)
		self.fields['color_verdadero'].required = True
		self.fields['turbiedad'].required = True
		self.fields['ph'].required = True
		self.fields['conductividad_electrica'].required = True

class PrimerPruebaUpdateForm4(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('coliformes_fecales', 'coliformes_totales')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm4, self).__init__(*args, **kwargs)
		self.fields['coliformes_fecales'].required = True
		self.fields['coliformes_totales'].required = True

class PrimerPruebaUpdateForm5(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('arsenico', 'hierro', 'manganeso', 'plomo',)
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm5, self).__init__(*args, **kwargs)
		self.fields['arsenico'].required = True
		self.fields['hierro'].required = True
		self.fields['manganeso'].required = True
		self.fields['plomo'].required = True

class PrimerPruebaUpdateForm6(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('floururos', 'nitratos', 'sulfatos', 'dureza_total', 'solidos_disueltos')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm6, self).__init__(*args, **kwargs)
		self.fields['floururos'].required = True
		self.fields['nitratos'].required = True
		self.fields['sulfatos'].required = True
		self.fields['dureza_total'].required = True
		self.fields['solidos_disueltos'].required = True

class PrimerPruebaUpdateForm7(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('creacion_reporte_analisis', 'resultados_laboratorio', 'validacion')
#		fields = ()

		widgets = {
			'creacion_reporte_analisis': forms.TextInput(attrs={'type':'date'}),
		}

	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm7, self).__init__(*args, **kwargs)
		self.fields['resultados_laboratorio'].required = True
		self.fields['creacion_reporte_analisis'].required = True
#		self.fields['validacion'].required = True

class PrimerPruebaUpdateForm8(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('validacion',)
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm8, self).__init__(*args, **kwargs)
#		self.fields['dictamen_sistema_potabilizador'].required = True
		self.fields['validacion'].required = True

class PrimerPruebaUpdateForm9(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('comparacion_color_verdadero', 'comparacion_turbiedad', 'comparacion_ph', 'comparacion_conductividad_electrica')

	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm9, self).__init__(*args, **kwargs)
		self.fields['comparacion_color_verdadero'].required = True
		self.fields['comparacion_turbiedad'].required = True
		self.fields['comparacion_ph'].required = True
		self.fields['comparacion_conductividad_electrica'].required = True

class PrimerPruebaUpdateForm10(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('comparacion_coliformes_fecales', 'comparacion_coliformes_totales')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm10, self).__init__(*args, **kwargs)
		self.fields['comparacion_coliformes_fecales'].required = True
		self.fields['comparacion_coliformes_totales'].required = True

class PrimerPruebaUpdateForm11(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('comparacion_arsenico', 'comparacion_hierro', 'comparacion_manganeso', 'comparacion_plomo',)
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm11, self).__init__(*args, **kwargs)
		self.fields['comparacion_arsenico'].required = True
		self.fields['comparacion_hierro'].required = True
		self.fields['comparacion_manganeso'].required = True
		self.fields['comparacion_plomo'].required = True

class PrimerPruebaUpdateForm12(forms.ModelForm):
	class Meta:
		model = PrimerPrueba
		fields = ('comparacion_floururos', 'comparacion_nitratos', 'comparacion_sulfatos', 'comparacion_dureza_total', 'comparacion_solidos_disueltos')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(PrimerPruebaUpdateForm12, self).__init__(*args, **kwargs)
		self.fields['comparacion_floururos'].required = True
		self.fields['comparacion_nitratos'].required = True
		self.fields['comparacion_sulfatos'].required = True
		self.fields['comparacion_dureza_total'].required = True
		self.fields['comparacion_solidos_disueltos'].required = True

"""Segunda Prueba de Calidad de Agua"""
class SegundaPruebaCreateForm(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('reporte_toma_agua', 'foto_toma_agua_1', 'foto_toma_agua_2', 'video_toma_agua')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(SegundaPruebaCreateForm, self).__init__(*args, **kwargs)
		self.fields['reporte_toma_agua'].required = True
		self.fields['foto_toma_agua_1'].required = True
		self.fields['foto_toma_agua_2'].required = True
		self.fields['video_toma_agua'].required = True

class SegundaPruebaUpdateForm1(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('registro_campo', 'cadena_custodia')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm1, self).__init__(*args, **kwargs)
		self.fields['registro_campo'].required = True
		self.fields['cadena_custodia'].required = True

class SegundaPruebaUpdateForm2(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('no_registro', )
#		fields = ()

	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm2, self).__init__(*args, **kwargs)
		self.fields['no_registro'].required = True

class SegundaPruebaUpdateForm3(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('color_verdadero', 'turbiedad', 'ph', 'conductividad_electrica')
	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm3, self).__init__(*args, **kwargs)
		self.fields['color_verdadero'].required = True
		self.fields['turbiedad'].required = True
		self.fields['ph'].required = True
		self.fields['conductividad_electrica'].required = True

class SegundaPruebaUpdateForm4(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('coliformes_fecales', 'coliformes_totales')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm4, self).__init__(*args, **kwargs)
		self.fields['coliformes_fecales'].required = True
		self.fields['coliformes_totales'].required = True

class SegundaPruebaUpdateForm5(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('arsenico', 'hierro', 'manganeso', 'plomo',)
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm5, self).__init__(*args, **kwargs)
		self.fields['arsenico'].required = True
		self.fields['hierro'].required = True
		self.fields['manganeso'].required = True
		self.fields['plomo'].required = True

class SegundaPruebaUpdateForm6(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('floururos', 'nitratos', 'sulfatos', 'dureza_total', 'solidos_disueltos')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm6, self).__init__(*args, **kwargs)
		self.fields['floururos'].required = True
		self.fields['nitratos'].required = True
		self.fields['sulfatos'].required = True
		self.fields['dureza_total'].required = True
		self.fields['solidos_disueltos'].required = True

class SegundaPruebaUpdateForm7(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('creacion_reporte_analisis', 'resultados_laboratorio', 'validacion')
#		fields = ()

		widgets = {
			'creacion_reporte_analisis': forms.TextInput(attrs={'type':'date'}),
		}

	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm7, self).__init__(*args, **kwargs)
		self.fields['resultados_laboratorio'].required = True
		self.fields['creacion_reporte_analisis'].required = True

class SegundaPruebaUpdateForm8(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('dictamen_validacion', 'validacion')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm8, self).__init__(*args, **kwargs)
		self.fields['dictamen_validacion'].required = True
		self.fields['validacion'].required = True

class SegundaPruebaUpdateForm9(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('comparacion_color_verdadero', 'comparacion_turbiedad', 'comparacion_ph', 'comparacion_conductividad_electrica')

	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm9, self).__init__(*args, **kwargs)
		self.fields['comparacion_color_verdadero'].required = True
		self.fields['comparacion_turbiedad'].required = True
		self.fields['comparacion_ph'].required = True
		self.fields['comparacion_conductividad_electrica'].required = True

class SegundaPruebaUpdateForm10(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('comparacion_coliformes_fecales', 'comparacion_coliformes_totales')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm10, self).__init__(*args, **kwargs)
		self.fields['comparacion_coliformes_fecales'].required = True
		self.fields['comparacion_coliformes_totales'].required = True

class SegundaPruebaUpdateForm11(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('comparacion_arsenico', 'comparacion_hierro', 'comparacion_manganeso', 'comparacion_plomo',)
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm11, self).__init__(*args, **kwargs)
		self.fields['comparacion_arsenico'].required = True
		self.fields['comparacion_hierro'].required = True
		self.fields['comparacion_manganeso'].required = True
		self.fields['comparacion_plomo'].required = True

class SegundaPruebaUpdateForm12(forms.ModelForm):
	class Meta:
		model = SegundaPrueba
		fields = ('comparacion_floururos', 'comparacion_nitratos', 'comparacion_sulfatos', 'comparacion_dureza_total', 'comparacion_solidos_disueltos')
#		fields = ()
	def __init__(self, *args, **kwargs):
		super(SegundaPruebaUpdateForm12, self).__init__(*args, **kwargs)
		self.fields['comparacion_floururos'].required = True
		self.fields['comparacion_nitratos'].required = True
		self.fields['comparacion_sulfatos'].required = True
		self.fields['comparacion_dureza_total'].required = True
		self.fields['comparacion_solidos_disueltos'].required = True		