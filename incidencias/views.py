from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import View
from accounts.models import *
from django.db.models import Q
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#Creación y consulta de incidencias
class CRViewIncidencias(View):
	@method_decorator(login_required)
	def get(self, request, pk=None):
		template_name = "incidencias/CRIncidencias.html"
		if pk:
			perfil = get_object_or_404(Perfil, pk=pk)
			escuela = User.objects.get(perfil=perfil)

			NuevaIncidenciaForm = IncidenciaCreateForm()
			incidencias = Incidencia.objects.filter(escuela=escuela)

		elif request.user.perfil.tipo == "Ejecutora":
			if request.user.perfil.cargo == "SIM":
				entidades = Entidad.objects.filter(sim=request.user.pk)
				zonas = Zona.objects.filter(entidad__in=entidades)
			if request.user.perfil.cargo == "RO":
				entidad = Entidad.objects.filter(residente_obra=request.user.pk)
				zonas = Zona.objects.filter(entidad=entidad)

			municipios = Municipio.objects.filter(zona__in=zonas)
			perfiles = Perfil.objects.filter(municipio__in=municipios)
			escuelas = User.objects.filter(perfil__in=perfiles)
			incidencias = Incidencia.objects.filter(escuela__in=escuelas)
			perfil=None
			escuela=None
			NuevaIncidenciaForm=None

		elif request.user.perfil.tipo == "PQ":
			incidencias = Incidencia.objects.filter(Q(fase="Primer prueba de calidad de agua") | Q(fase="Segunda prueba de calidad de agua"))
			perfil=None
			escuela=None
			NuevaIncidenciaForm = None
		else:
			perfil=None
			escuela=None
			NuevaIncidenciaForm = None
			incidencias = Incidencia.objects.all()

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
	@method_decorator(login_required)
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