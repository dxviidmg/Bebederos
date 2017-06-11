from django.shortcuts import render
from django.views.generic import View
from .models import *

class ListViewPlantillas(View):
	def get(self, request):
		template_name = "evidencias/ListViewPlantillas.html"

		plantillas = Plantilla.objects.all()

		context = {
			'plantillas': plantillas
		}
		return render(request,template_name, context)