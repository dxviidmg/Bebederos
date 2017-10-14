from django.shortcuts import render
from django.views.generic import View
from .models import *
class ListViewPlantillas(View):
#	@method_decorator(login_required)
	def get(self, request):
		template_name = "plantillas/listPlantillas.html"	
		plantillas = Plantilla.objects.all()
		context = {
			'plantillas': plantillas,
		}
		return render(request,template_name, context)