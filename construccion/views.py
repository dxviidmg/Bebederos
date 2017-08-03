from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from accounts.models import Perfil
from django.contrib.auth.models import User
from .forms import *

#Creación y edición de la visita de acuerdo
class ViewInicioDeTrabajo(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "construccion/createInicioDeTrabajo.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevoInicioForm = InicioDeTrabajoCreateForm()

		try:
			inicio = InicioDeTrabajo.objects.get(escuela=escuela)
			EdicionInicioForm = InicioDeTrabajoEditForm(instance=inicio)
		except InicioDeTrabajo.DoesNotExist:
			inicio = None
			EdicionInicioForm = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevoInicioForm': NuevoInicioForm,
			'inicio': inicio,
			'EdicionInicioForm': EdicionInicioForm
		}
		return render(request, template_name, context)
#	def post(self, request, pk):
#		perfil = get_object_or_404(Perfil, pk=pk)
#		escuela = User.objects.get(perfil=perfil)
#		NuevaVisitaForm = VisitaDeAcuerdoCreateForm(data=request.POST, files=request.FILES)
#		sim = User.objects.get(pk=request.user.pk)

#		if NuevaVisitaForm.is_valid():
#			NuevaVisita = NuevaVisitaForm.save(commit=False)
#			NuevaVisita.escuela = escuela
#			NuevaVisita.sim = sim
#			NuevaVisitaForm.save()

#		try:
#			visita = VisitaDeAcuerdo.objects.get(escuela=escuela)
#			EdicionVisitaForm = VisitaDeAcuerdoEditForm(instance=visita, data=request.POST, files=request.FILES)

#			if EdicionVisitaForm.is_valid():
#				EdicionVisitaForm.save()

#		except VisitaAlSitio.DoesNotExist:
#			visita = None
#			EdicionVisitaAlSitioForm = None

#		return redirect("accounts:DetailViewEscuela", pk=perfil.pk)		