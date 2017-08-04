from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from accounts.models import Perfil
from django.contrib.auth.models import User
from .forms import *

class ViewPrimerPrueba(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "pruebasAgua/createPrimerPrueba.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaPruebaForm = PrimerPruebaCreateForm()

#		try:
#			inicio = InicioDeTrabajo.objects.get(escuela=escuela)
#			EdicionInicioForm = InicioDeTrabajoEditForm(instance=inicio)
#		except InicioDeTrabajo.DoesNotExist:
#			inicio = None
#			EdicionInicioForm = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevaPruebaForm': NuevaPruebaForm,
#			'inicio': inicio,
#			'EdicionInicioForm': EdicionInicioForm
		}
		return render(request, template_name, context)