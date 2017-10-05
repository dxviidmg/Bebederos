from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from accounts.models import Perfil
from django.contrib.auth.models import User
from .forms import *

#Creación y edición de la visita de acuerdo
class CRViewInicioDeTrabajo(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "construccion/CRInicioDeTrabajo.html"
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

		return redirect("construccion:CRViewInicioDeTrabajo", pk=perfil.pk)

class CRViewTerminoDeTrabajo(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "construccion/CRTerminoDeTrabajo.html"
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

class CRViewEvidencias(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "construccion/CREvidencias.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)

		evidencias = EvidenciaConstruccion.objects.filter(escuela=escuela)
		evidenciaFinal = evidencias.filter(fase="Instalación de Mueble Bebedero", aprobacion_SI="Aprobado")

		NuevaEvidenciaForm = EvidenciaConstruccionCreateForm()

		NuevaInstalacionForm = InstalacionBebederoCreateForm()
		
		try:
			instalacion = InstalacionBebedero.objects.get(escuela=escuela)
		except InstalacionBebedero.DoesNotExist:
			instalacion = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'evidencias': evidencias,
			'NuevaEvidenciaForm': NuevaEvidenciaForm,
			'NuevaInstalacionForm': NuevaInstalacionForm,
			'instalacion': instalacion,
			'evidenciaFinal': evidenciaFinal,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)

		bitacora = EvidenciaConstruccion.objects.filter(escuela=escuela)
		NuevaEvidenciaForm = EvidenciaConstruccionCreateForm(data=request.POST, files=request.FILES)
		ejecutora = User.objects.get(pk=request.user.pk)
		
		if NuevaEvidenciaForm.is_valid():
			NuevaEvidencia = NuevaEvidenciaForm.save(commit=False)
			NuevaEvidencia.escuela = escuela
			NuevaEvidencia.ejecutora = ejecutora
			NuevaEvidencia.save()

		NuevaInstalacionForm = InstalacionBebederoCreateForm(data=request.POST, files=request.FILES)
		si = User.objects.get(pk=request.user.pk)

		if NuevaInstalacionForm.is_valid():
			NuevaInstalacion = NuevaInstalacionForm.save(commit=False)
			NuevaInstalacion.escuela = escuela
			NuevaInstalacion.si = si
			NuevaInstalacion.save()
			
		return redirect("construccion:CRViewEvidencias", pk=perfil.pk)



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
	def post(self, request, pk):
		evidencia = get_object_or_404(EvidenciaConstruccion, pk=pk)

		escuela = User.objects.get(escuela_evidencia=evidencia)
		perfil = Perfil.objects.get(user_id=escuela)

		EdicionEvidenciaForm=EvidenciaConstruccionEditForm(instance=evidencia, data=request.POST)
		if EdicionEvidenciaForm.is_valid:
			EdicionEvidenciaForm.save()

		return redirect("construccion:CRViewEvidencias", pk=perfil.pk)