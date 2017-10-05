from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import *
from django.core.urlresolvers import reverse_lazy
from accounts.models import Perfil
from .forms import *
from django.contrib.auth.models import User

#Creación y edición de la visita de acuerdo
class CRViewVisitaDeAcuerdo(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "visitas/CRVisitaDeAcuerdo.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaVisitaForm=VisitaDeAcuerdoCreateForm()

		try:
			visita = VisitaDeAcuerdo.objects.get(escuela=escuela)
			CompleteNuevaVisitaForm = VisitaDeAcuerdoEditForm(instance=visita)
		except VisitaDeAcuerdo.DoesNotExist:
			visita = None
			CompleteNuevaVisitaForm = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevaVisitaForm': NuevaVisitaForm,
			'visita': visita,
			'CompleteNuevaVisitaForm': CompleteNuevaVisitaForm,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaVisitaForm = VisitaDeAcuerdoCreateForm(data=request.POST, files=request.FILES)
		si = User.objects.get(pk=request.user.pk)

		if NuevaVisitaForm.is_valid():
			NuevaVisita = NuevaVisitaForm.save(commit=False)
			NuevaVisita.escuela = escuela
			NuevaVisita.si = si
			NuevaVisita.save()

		try:
			visita = VisitaDeAcuerdo.objects.get(escuela=escuela)
			CompleteNuevaVisitaForm = VisitaDeAcuerdoEditForm(instance=visita, data=request.POST, files=request.FILES)
			if CompleteNuevaVisitaForm.is_valid():
				CompleteNuevaVisitaForm.save()
	
		except VisitaDeAcuerdo.DoesNotExist:
			visita = None
			CompleteNuevaVisitaForm = None

		return redirect("visitas:CRViewVisitaDeAcuerdo", pk=perfil.pk)

#Creación y edición de inicio de funcionamiento
class CRViewInicioFuncionamiento(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "visitas/CRVInicioFuncionamiento.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevoFuncionamientoForm=InicioFuncionamientoCreateForm()

		try:
			funcionamiento = InicioFuncionamiento.objects.get(escuela=escuela)
		except InicioFuncionamiento.DoesNotExist:
			funcionamiento = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevoFuncionamientoForm': NuevoFuncionamientoForm,
			'funcionamiento': funcionamiento,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevoFuncionamientoForm=InicioFuncionamientoCreateForm(data=request.POST, files=request.FILES)
		si = User.objects.get(pk=request.user.pk)

		if NuevoFuncionamientoForm.is_valid():
			NuevoFuncionamiento = NuevoFuncionamientoForm.save(commit=False)
			NuevoFuncionamiento.escuela = escuela
			NuevoFuncionamiento.si = si
			NuevoFuncionamiento.save()

		return redirect("visitas:CRViewInicioFuncionamiento", pk=perfil.pk)		