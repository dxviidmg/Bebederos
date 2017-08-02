from django import forms
from .models import *

class VisitaAlSitioCreateForm(forms.ModelForm):
	class Meta:
		model = VisitaAlSitio
		fields = ('constancia_visita', 'hoja_cotizacion', 'plantilla_fotografica', 'membrete_mail', 'agenda')