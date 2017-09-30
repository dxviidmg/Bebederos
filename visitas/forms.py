from django import forms
from .models import *

my_default_errors = {
    'required': 'Este campo es necesario',
    'invalid': 'Introduzca un dato valido'
	}

class VisitaDeAcuerdoCreateForm(forms.ModelForm):
	class Meta:
		model = VisitaDeAcuerdo
		fields = ('convenio_concertacion', 'cedula_identificacion', 'acta_acuerdos', 'constancia_integracion_comite')
		#fields = ()

class VisitaDeAcuerdoEditForm(forms.ModelForm):
	class Meta:
		model = VisitaDeAcuerdo
		fields = ('plano_instalacion_electrica', 'plano_instalacion_hidraulica', 'plano_instalacion_sanitaria', 'estimacion',)
		#fields = ()
	def __init__(self, *args, **kwargs):
		super(VisitaDeAcuerdoEditForm, self).__init__(*args, **kwargs)
		self.fields['plano_instalacion_electrica'].required = True
		self.fields['plano_instalacion_hidraulica'].required = True
		self.fields['plano_instalacion_sanitaria'].required = True
		self.fields['estimacion'].required = True

class EntregaDeBebederoCreateForm(forms.ModelForm):
	class Meta:
		model = EntregaDeBebedero
		fields = ('acta_funcionamiento', 'convenio_responsabilidades', 'video')
		#fields = ()