from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import View
from accounts.models import Perfil
from django.db.models import Q
from .forms import *
#Creación y edición de la visita de acuerdo
class ViewIncidencias(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "incidencias/createIncidencias.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)

		NuevaIncidenciaForm = IncidenciaCreateForm()

		incidencias = Incidencia.objects.filter(escuela=escuela)
		incidenciasActuales = incidencias.filter(Q(status="En espera") | Q(status="Atendiendo"))
		historialIncidencias = incidencias.filter(status="Solucionado")

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'incidenciasActuales': incidenciasActuales,
			'historialIncidencias': historialIncidencias,
			'NuevaIncidenciaForm': NuevaIncidenciaForm,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaIncidenciaForm = IncidenciaCreateForm(data=request.POST, files=request.FILES)
		autor = User.objects.get(pk=request.user.pk)

		if NuevaIncidenciaForm.is_valid():
			NuevaIncidencia = NuevaIncidenciaForm.save(commit=False)
			NuevaIncidencia.escuela = escuela
			NuevaIncidencia.autor = autor
			NuevaIncidencia.save()

		return redirect("accounts:DetailViewEscuela", pk=perfil.pk)