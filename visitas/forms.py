from django import forms
from .models import *

class VisitaAlSitioCreateForm(forms.ModelForm):
	class Meta:
		model = VisitaAlSitio
		fields = ('acta_visita', 'copia_INE',)
		#fields = ()

class VisitaAlSitioEditForm(forms.ModelForm):
	class Meta:
		model = VisitaAlSitio
		fields = ('acta_visita', 'copia_INE',)
		#fields = ()

class VisitaDeAcuerdoCreateForm(forms.ModelForm):
	class Meta:
		model = VisitaDeAcuerdo
		fields = ('convenio_concertacion', 'cedula_identificacion', 'acta_acuerdos', 'constancia_integracion_comite')
		#fields = ()

class VisitaDeAcuerdoEditForm(forms.ModelForm):
	class Meta:
		model = VisitaDeAcuerdo
		fields = ('convenio_concertacion', 'cedula_identificacion', 'acta_acuerdos', 'constancia_integracion_comite')
		#fields = ()

class EntregaDeBebederoCreateForm(forms.ModelForm):
	class Meta:
		model = EntregaDeBebedero
		fields = ('acta_entrega', 'convenio_responsabilidades', 'constancia_entrega_llaves', 'video')
		#fields = ()

class EntregaDeBebederoEditForm(forms.ModelForm):
	class Meta:
		model = EntregaDeBebedero
		fields = ('acta_entrega', 'convenio_responsabilidades', 'constancia_entrega_llaves', 'video')	