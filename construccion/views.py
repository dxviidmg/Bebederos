from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from accounts.models import Perfil
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#Creación, edición y detalle de una visita de acuerdo
class CRViewInicioDeTrabajo(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "construccion/CRInicioDeTrabajo.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevoInicioForm = InicioDeTrabajoCreateForm()

		try:
			inicio = InicioDeTrabajo.objects.get(escuela=escuela)
			EdicionInicioForm = InicioDeTrabajoCreateForm(instance=inicio)
		except InicioDeTrabajo.DoesNotExist:
			inicio = None
			EdicionInicioForm = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevoInicioForm': NuevoInicioForm,
			'inicio': inicio,
			'EdicionInicioForm': EdicionInicioForm,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevoInicioForm = InicioDeTrabajoCreateForm(data=request.POST, files=request.FILES)
		si = User.objects.get(pk=request.user.pk)

		try:
			inicio = InicioDeTrabajo.objects.get(escuela=escuela)
			EdicionInicioForm = InicioDeTrabajoCreateForm(instance=inicio, files=request.FILES)

			if EdicionInicioForm.is_valid():
				EdicionInicioForm.save()

		except InicioDeTrabajo.DoesNotExist:
			inicio = None
			EdicionInicioForm = None

			if NuevoInicioForm.is_valid():
				NuevoInicio = NuevoInicioForm.save(commit=False)
				NuevoInicio.escuela = escuela
				NuevoInicio.si = si
				NuevoInicio.save()

		return redirect("construccion:CRViewInicioDeTrabajo", pk=perfil.pk)

#Creación, edición y detalle de un termino de trabajos
class CRViewTerminoDeTrabajo(View):
	@method_decorator(login_required)
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

#Creación, edición y lista de evidencias de construcción 
class CRViewEvidencias(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "construccion/CREvidencias.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		perfil.UpdateEvidenciasCount()
		perfil.UpdateAvance()

		escuela = User.objects.get(perfil=perfil)

		evidencias = EvidenciaConstruccion.objects.filter(escuela=escuela).order_by("fase")
#		evidencias = evidencias.extra(select={'myinteger': 'CAST(fase AS INTEGER)'}).order_by('myinteger')
#		print(e2) 

		NuevaEvidenciaForm = EvidenciaConstruccionCreateForm()
		NuevaEnvolventeForm = EnvolventeTerminadaCreateForm()
		
		try:
			envolvente = EnvolventeTerminada.objects.get(escuela=escuela)
		except EnvolventeTerminada.DoesNotExist:
			envolvente = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'evidencias': evidencias,
			'NuevaEvidenciaForm': NuevaEvidenciaForm,
			'NuevaEnvolventeForm': NuevaEnvolventeForm,
			'envolvente': envolvente,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)

		NuevaEvidenciaForm = EvidenciaConstruccionCreateForm(data=request.POST, files=request.FILES)
		
		if NuevaEvidenciaForm.is_valid():
			NuevaEvidencia = NuevaEvidenciaForm.save(commit=False)
			NuevaEvidencia.escuela = escuela
			NuevaEvidencia.save()
			messages.success(request, "Actualización exitosa")			
			perfil.UpdateEvidenciasCount()
			
		NuevaEnvolventeForm = EnvolventeTerminadaCreateForm(data=request.POST, files=request.FILES)
		si = User.objects.get(pk=request.user.pk)

		if NuevaEnvolventeForm.is_valid():
			NuevaEnvolvente = NuevaEnvolventeForm.save(commit=False)
			NuevaEnvolvente.escuela = escuela
			NuevaEnvolvente.si = si
			NuevaEnvolvente.save()
			messages.success(request, "Actualización exitosa")

		return redirect("construccion:CRViewEvidencias", pk=perfil.pk)

#Actualización de una evidencia
class UpdateViewEvidencia(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "construccion/updateEvidencia.html"
		evidencia = get_object_or_404(EvidenciaConstruccion, pk=pk)
		EdicionEvidenciaForm = EvidenciaConstruccionCreateForm(instance=evidencia)
		EdicionEvidenciaForm2 = EvidenciaConstruccionEditForm(instance=evidencia)
		escuela = User.objects.get(escuela_evidencia=evidencia)
		perfil = Perfil.objects.get(user_id=escuela)

		context = {
			'evidencia': evidencia,
			'EdicionEvidenciaForm': EdicionEvidenciaForm,
			'EdicionEvidenciaForm2': EdicionEvidenciaForm2,	
			'escuela': escuela,
			'perfil': perfil,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		evidencia = get_object_or_404(EvidenciaConstruccion, pk=pk)

		escuela = User.objects.get(escuela_evidencia=evidencia)
		perfil = Perfil.objects.get(user_id=escuela)
		
		EdicionEvidenciaForm=EvidenciaConstruccionCreateForm(instance=evidencia, data=request.POST, files=request.FILES)
		if EdicionEvidenciaForm.is_valid():
			EdicionEvidenciaForm.save()

		EdicionEvidenciaForm2=EvidenciaConstruccionEditForm(instance=evidencia, data=request.POST, files=request.FILES)
		if EdicionEvidenciaForm2.is_valid():
			EdicionEvidenciaForm2.save()
			perfil.UpdateAvance()

		return redirect("construccion:CRViewEvidencias", pk=perfil.pk)