from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import View
from accounts.models import Perfil

#Creación y edición de la visita de acuerdo
class ViewIncidencias(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "incidencias/createIncidencias.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
#		NuevoInicioForm = InicioDeTrabajoCreateForm()
		incidencias = Incidencia.objects.filter(escuela=escuela)
		print(incidencias)

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'incidencias': incidencias,
#			'NuevoInicioForm': NuevoInicioForm,
#			'inicio': inicio,
#			'EdicionInicioForm': EdicionInicioForm
		}
		return render(request, template_name, context)
#	def post(self, request, pk):
#		perfil = get_object_or_404(Perfil, pk=pk)
#		escuela = User.objects.get(perfil=perfil)
#		NuevoInicioForm = InicioDeTrabajoCreateForm(data=request.POST, files=request.FILES)
#		sim = User.objects.get(pk=request.user.pk)

#		if NuevoInicioForm.is_valid():
#			NuevoInicio = NuevoInicioForm.save(commit=False)
#			NuevoInicio.escuela = escuela
#			NuevoInicio.sim = sim
#			NuevoInicio.save()

#		try:
#			inicio = InicioDeTrabajo.objects.get(escuela=escuela)
#			EdicionInicioForm = InicioDeTrabajoEditForm(instance=inicio, data=request.POST, files=request.FILES)
#			if EdicionInicioForm.is_valid():
#				EdicionInicioForm.save()

#		except InicioDeTrabajo.DoesNotExist:
#			inicio = None
#			EdicionInicioForm = None

#		return redirect("accounts:DetailViewEscuela", pk=perfil.pk)