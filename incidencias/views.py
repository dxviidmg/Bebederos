from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import View
from accounts.models import Perfil
from django.db.models import Q
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages

#Creación y consulta de incidencias
class CRViewIncidencias(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "incidencias/CRIncidencias.html"
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
			messages.success(request, "Registro exitoso")

		return redirect("incidencias:CRViewIncidencias", pk=perfil.pk)

#Actualización de una incidencia
class UpdateViewIncidencia(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "incidencias/updateIncidencia.html"
		incidencia = get_object_or_404(Incidencia, pk=pk)
		EdicionIncidenciaForm = IncidenciaEditForm(instance=incidencia)
		escuela = User.objects.get(escuela_incidencia=incidencia)
		perfil = Perfil.objects.get(user_id=escuela)

		context = {
			'incidencia': incidencia,
			'EdicionIncidenciaForm': EdicionIncidenciaForm,
			'escuela': escuela,
			'perfil': perfil,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		incidencia = get_object_or_404(Incidencia, pk=pk)
		escuela = User.objects.get(escuela_incidencia=incidencia)
		perfil = Perfil.objects.get(user_id=escuela)

		EdicionIncidenciaForm=IncidenciaEditForm(instance=incidencia, data=request.POST)
		if EdicionIncidenciaForm.is_valid:
			EdicionIncidenciaForm.save()
			messages.success(request, "Actualización exitosa")

		return redirect("incidencias:UpdateViewIncidencia", pk=incidencia.pk)