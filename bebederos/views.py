from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from accounts.models import Perfil
from .forms import *

#Creación y edición de la visita de acuerdo
class ViewBebederos(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "bebederos/createBebedero.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)

		sistemaBebedero = SistemaBebedero.objects.get(escuela=escuela)

		BebederoForm = BebederoCreateOrEditForm(instance=sistemaBebedero)

#		try:
#			inicio = InicioDeTrabajo.objects.get(escuela=escuela)
#			EdicionInicioForm = InicioDeTrabajoEditForm(instance=inicio)
#		except InicioDeTrabajo.DoesNotExist:
#			inicio = None
#			EdicionInicioForm = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'BebederoForm': BebederoForm,
#			'NuevoInicioForm': NuevoInicioForm,
#			'inicio': inicio,
#			'EdicionInicioForm': EdicionInicioForm
		}
		return render(request, template_name, context)