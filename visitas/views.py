from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import *
from django.core.urlresolvers import reverse_lazy
from accounts.models import Perfil
from .forms import *
from django.contrib.auth.models import User

#Creación de un Capitulo
class CreateViewVisitaAlSitio(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "visitas/createVisitaAlSitio.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)

		try:
			visita = VisitaAlSitio.objects.get(escuela=escuela)
			EdicionVisitaForm=VisitaAlSitioEditForm(instance=visita)
		except VisitaAlSitio.DoesNotExist:
			visita = None
			EdicionVisitaForm = None

		NuevaVisitaForm=VisitaAlSitioCreateForm()
		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevaVisitaForm': NuevaVisitaForm,
			'visita': visita,
			'EdicionVisitaForm': EdicionVisitaForm
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaVisitaForm=VisitaAlSitioCreateForm(data=request.POST, files=request.FILES)
		sim = User.objects.get(pk=request.user.pk)

		if NuevaVisitaForm.is_valid():
			NuevaVisita = NuevaVisitaForm.save(commit=False)
			NuevaVisita.escuela = escuela
			NuevaVisita.sim = sim
			NuevaVisitaForm.save()

		try:
			visita = VisitaAlSitio.objects.get(escuela=escuela)
			EdicionVisitaForm = VisitaAlSitioEditForm(instance=visita, data=request.POST, files=request.FILES)

			if EdicionVisitaForm.is_valid():
				EdicionVisitaForm.save()

		except VisitaAlSitio.DoesNotExist:
			visita = None
			EdicionVisitaAlSitioForm = None



		return redirect("accounts:DetailViewEscuela", pk=perfil.pk)