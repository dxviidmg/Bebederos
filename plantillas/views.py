from django.shortcuts import render
from django.views.generic import View
from .models import *

#Consulta de plantillas por tipo de usuario
class ListViewPlantillas(View):
#	@method_decorator(login_required)
	def get(self, request):
		template_name = "plantillas/listPlantillas.html"	
		user = User.objects.get(pk=request.user.pk)
		perfil = Perfil.objects.get(user=user)
		plantillas = Plantilla.objects.filter(tipo_usuario=perfil.tipo)
		context = {
			'plantillas': plantillas,
		}
		return render(request,template_name, context)