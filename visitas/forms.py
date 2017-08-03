from django import forms
from .models import *

class VisitaAlSitioCreateForm(forms.ModelForm):
	class Meta:
		model = VisitaAlSitio
		fields = ('constancia_visita', 'hoja_cotizacion', 'plantilla_fotografica', 'membrete_mail', 'agenda')

class VisitaAlSitioEditForm(forms.ModelForm):
#	constancia_visita = forms.ImageField(required=False, widget=forms.FileInput)
#	hoja_cotizacion = forms.ImageField(required=False, widget=forms.FileInput)
#	plantilla_fotografica = forms.ImageField(required=False, widget=forms.FileInput)
#	membrete_mail = forms.ImageField(required=False, widget=forms.FileInput)
#	agenda = forms.ImageField(required=False, widget=forms.FileInput)

	class Meta:
		model = VisitaAlSitio
		fields = ('constancia_visita', 'hoja_cotizacion', 'plantilla_fotografica', 'membrete_mail', 'agenda')	