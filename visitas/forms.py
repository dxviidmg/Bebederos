from django import forms
from .models import *

my_default_errors = {
    'required': 'Este campo es necesario',
    'invalid': 'Introduzca un dato valido'
	}

class VisitaDeAcuerdoCreateForm(forms.ModelForm):
	class Meta:
		model = VisitaDeAcuerdo
		fields = ('cedula_identificacion', 'acta_ubicacion', 'convenio_concertacion', 'constancia_integracion_comite', 'plano_conjunto', 'distribucion_planta', 'memoria_calculo_1', 'memoria_calculo_2', 'memoria_calculo_3', 'isometrico_instalacion',)
		#fields = ()
#	def __init__(self, *args, **kwargs):
#		super(VisitaDeAcuerdoCreateForm, self).__init__(*args, **kwargs)
#		self.fields['convenio_concertacion'].required = True
#		self.fields['cedula_identificacion'].required = True
#		self.fields['acta_acuerdos'].required = True
#		self.fields['croquis_modulo'].required = True	
#		self.fields['convenio_concertacion'].required = True
#		self.fields['memoria_calculo'].required = True
#		self.fields['plano_conjunto'].required = True
#		self.fields['distribucion_planta'].required = True
#		self.fields['plano_instalacion_electrica'].required = True
#		self.fields['plano_instalacion_hidraulica'].required = True
#		self.fields['plano_instalacion_sanitaria'].required = True

class InicioFuncionamientoCreateForm(forms.ModelForm):
	class Meta:
		model = InicioFuncionamiento
		fields = ('acta_funcionamiento', 'recibo_llaves', 'foto')
		#fields = ()

class ActaEntregaCreateForm (forms.ModelForm):
	class Meta:
		model = ActaEntrega
		fields = ('acta_entrega',)	