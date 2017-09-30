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
		except InicioDeTrabajo.DoesNotExist:
			inicio = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevoInicioForm': NuevoInicioForm,
			'inicio': inicio,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevoInicioForm = InicioDeTrabajoCreateForm(data=request.POST, files=request.FILES)
		si = User.objects.get(pk=request.user.pk)

		if NuevoInicioForm.is_valid():
			NuevoInicio = NuevoInicioForm.save(commit=False)
			NuevoInicio.escuela = escuela
			NuevoInicio.si = si
			NuevoInicio.save()

		return redirect("construccion:ViewInicioDeTrabajo", pk=perfil.pk)

#Creación y edición de la instalación de un bebedero
class ViewInstalacionBebedero(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "construccion/createInstalacionBebedero.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaInstalacionForm = InstalacionBebederoCreateForm()
		#evidencias = EvidenciaC
		try:
			instalacion = InstalacionBebedero.objects.get(escuela=escuela)
		except InstalacionBebedero.DoesNotExist:
			instalacion = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevaInstalacionForm': NuevaInstalacionForm,
			'instalacion': instalacion,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaInstalacionForm = InstalacionBebederoCreateForm(data=request.POST, files=request.FILES)
		si = User.objects.get(pk=request.user.pk)

		if NuevaInstalacionForm.is_valid():
			NuevaInstalacion = NuevaInstalacionForm.save(commit=False)
			NuevaInstalacion.escuela = escuela
			NuevaInstalacion.si = si
			NuevaInstalacion.save()

		return redirect("construccion:ViewInstalacionBebedero", pk=perfil.pk)

class ViewTerminoDeTrabajo(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "construccion/createTerminoDeTrabajo.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevoTerminoForm = TerminoDeTrabajoCreateForm()

		try:
			termino = TerminoDeTrabajo.objects.get(escuela=escuela)
		except TerminoDeTrabajo.DoesNotExist:
			termino = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevoTerminoForm': NuevoTerminoForm,
			'termino': termino,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevoTerminoForm = TerminoDeTrabajoCreateForm(data=request.POST, files=request.FILES)
		si = User.objects.get(pk=request.user.pk)

		if NuevoTerminoForm.is_valid():
			NuevoTermino = NuevoTerminoForm.save(commit=False)
			NuevoTermino.escuela = escuela
			NuevoTermino.si = si
			NuevoTermino.save()

		return redirect("construccion:ViewTerminoDeTrabajo", pk=perfil.pk)

class ViewBitacora(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "construccion/createBitacora.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)

		bitacora = EvidenciaConstruccion.objects.filter(escuela=escuela)
		NuevaEvidenciaForm = EvidenciaConstruccionCreateForm()

		notas = NotaDeBitacora.objects.filter(escuela=escuela)
		NuevaNotaForm = NotaDeBitacoraCreateForm()
		context = {
			'perfil': perfil,
			'escuela': escuela,
			'bitacora': bitacora,
			'NuevaEvidenciaForm': NuevaEvidenciaForm,
			'notas': notas,
			'NuevaNotaForm': NuevaNotaForm,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)

		bitacora = EvidenciaConstruccion.objects.filter(escuela=escuela)
		NuevaEvidenciaForm = EvidenciaConstruccionCreateForm(data=request.POST, files=request.FILES)
		ejecutora = User.objects.get(pk=request.user.pk)
		
		NuevaNotaForm = NotaDeBitacoraCreateForm(data=request.POST)
		autor = User.objects.get(pk=request.user.pk)
		
		if NuevaEvidenciaForm.is_valid():
			NuevaEvidencia = NuevaEvidenciaForm.save(commit=False)
			NuevaEvidencia.escuela = escuela
			NuevaEvidencia.ejecutora = ejecutora
			NuevaEvidencia.save()

		if NuevaNotaForm.is_valid():
			NuevaNota = NuevaNotaForm.save(commit=False)
			NuevaNota.escuela = escuela
			NuevaNota.autor = autor
			NuevaNota.save()
		return redirect("construccion:ViewBitacora", pk=perfil.pk)



class UpdateViewEvidencia(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "construccion/updateEvidencia.html"
		evidencia = get_object_or_404(EvidenciaConstruccion, pk=pk)
		EdicionEvidenciaForm = EvidenciaConstruccionEditForm(instance=evidencia)
		escuela = User.objects.get(escuela_evidencia=evidencia)
		perfil = Perfil.objects.get(user_id=escuela)

		context = {
			'evidencia': evidencia,
			'EdicionEvidenciaForm': EdicionEvidenciaForm,
			'escuela': escuela,
			'perfil': perfil,
		}
		return render(request, template_name, context)
#	def post(self, request, pk):
#		incidencia = get_object_or_404(Incidencia, pk=pk)
#		EdicionIncidenciaForm = IncidenciaEditForm(instance=incidencia)
#		escuela = User.objects.get(escuela_incidencia=incidencia)
#		perfil = Perfil.objects.get(user_id=escuela)

#		EdicionIncidenciaForm=IncidenciaEditForm(instance=incidencia, data=request.POST)
#		if EdicionIncidenciaForm.is_valid:
#			EdicionIncidenciaForm.save()

#		return redirect("incidencias:ViewIncidencias", pk=perfil.pk)		