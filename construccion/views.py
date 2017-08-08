from django.shortcuts import render, get_object_or_404, redirect
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
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevoInicioForm = InicioDeTrabajoCreateForm(data=request.POST, files=request.FILES)
		sim = User.objects.get(pk=request.user.pk)

		if NuevoInicioForm.is_valid():
			NuevoInicio = NuevoInicioForm.save(commit=False)
			NuevoInicio.escuela = escuela
			NuevoInicio.sim = sim
			NuevoInicio.save()

		try:
			inicio = InicioDeTrabajo.objects.get(escuela=escuela)
			EdicionInicioForm = InicioDeTrabajoEditForm(instance=inicio, data=request.POST, files=request.FILES)

			if EdicionInicioForm.is_valid():
				EdicionInicioForm.save()

		except InicioDeTrabajo.DoesNotExist:
			inicio = None
			EdicionInicioForm = None

		return redirect("accounts:DetailViewEscuela", pk=perfil.pk)

#Creación y edición de la instalación de un bebedero
class ViewInstalacionBebedero(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "construccion/createInstalacionBebedero.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaInstalacionForm = InstalacionBebederoCreateForm()

		try:
			instalacion = InstalacionBebedero.objects.get(escuela=escuela)
			EdicionInstalacionForm = InstalacionBebederoEditForm(instance=instalacion)
		except InstalacionBebedero.DoesNotExist:
			instalacion = None
			EdicionInstalacionForm = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevaInstalacionForm': NuevaInstalacionForm,
			'instalacion': instalacion,
			'EdicionInstalacionForm': EdicionInstalacionForm
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaInstalacionForm = InstalacionBebederoCreateForm(data=request.POST, files=request.FILES)
		sim = User.objects.get(pk=request.user.pk)

		if NuevaInstalacionForm.is_valid():
			NuevaInstalacion = NuevaInstalacionForm.save(commit=False)
			NuevaInstalacion.escuela = escuela
			NuevaInstalacion.sim = sim
			NuevaInstalacion.save()

		try:
			instalacion = InstalacionBebedero.objects.get(escuela=escuela)
			EdicionInstalacionForm = InstalacionBebederoEditForm(instance=instalacion, data=request.POST, files=request.FILES)

			if EdicionInstalacionForm.is_valid():
				EdicionInstalacionForm.save()

		except InstalacionBebedero.DoesNotExist:
			instalacion = None
			EdicionInstalacionForm = None

		return redirect("accounts:DetailViewEscuela", pk=perfil.pk)

class ViewTerminoDeTrabajo(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "construccion/createTerminoDeTrabajo.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevoTerminoForm = TerminoDeTrabajoCreateForm()

		try:
			termino = TerminoDeTrabajo.objects.get(escuela=escuela)
			EdicionTerminoForm = InicioDeTrabajoEditForm(instance=termino)
		except TerminoDeTrabajo.DoesNotExist:
			termino = None
			EdicionTerminoForm = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevoTerminoForm': NuevoTerminoForm,
			'termino': termino,
			'EdicionTerminoForm': EdicionTerminoForm
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevoTerminoForm = TerminoDeTrabajoCreateForm(data=request.POST, files=request.FILES)
		sim = User.objects.get(pk=request.user.pk)

		if NuevoTerminoForm.is_valid():
			NuevoTermino = NuevoTerminoForm.save(commit=False)
			NuevoTermino.escuela = escuela
			NuevoTermino.sim = sim
			NuevoTermino.save()

		try:
			termino = TerminoDeTrabajo.objects.get(escuela=escuela)
			EdicionTerminoForm = TerminoDeTrabajoEditForm(instance=termino, data=request.POST, files=request.FILES)

			if EdicionTerminoForm.is_valid():
				EdicionTerminoForm.save()

		except TerminoDeTrabajo.DoesNotExist:
			termino = None
			EdicionTerminoForm = None

		return redirect("accounts:DetailViewEscuela", pk=perfil.pk)		