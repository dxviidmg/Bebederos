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
		except VisitaDeAcuerdo.DoesNotExist:
			visita = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevaVisitaForm': NuevaVisitaForm,
			'visita': visita,
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
	
		except VisitaDeAcuerdo.DoesNotExist:
			visita = None

		return redirect("visitas:CRViewVisitaDeAcuerdo", pk=perfil.pk)

#Creación y edición de inicio de funcionamiento
class CRViewInicioFuncionamiento(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "visitas/CRInicioFuncionamiento.html"
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

#Creación y edición de inicio de funcionamiento
class CRViewActaEntrega(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "visitas/CRActaEntrega.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaActaEntregaForm=ActaEntregaCreateForm()

		try:
			actaEntrega = ActaEntrega.objects.get(escuela=escuela)
		except ActaEntrega.DoesNotExist:
			actaEntrega = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevaActaEntregaForm': NuevaActaEntregaForm,
			'actaEntrega': actaEntrega,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaActaEntregaForm=ActaEntregaCreateForm(data=request.POST, files=request.FILES)
		si = User.objects.get(pk=request.user.pk)

		if NuevaActaEntregaForm.is_valid():
			NuevaActaEntrega = NuevaActaEntregaForm.save(commit=False)
			NuevaActaEntrega.escuela = escuela
			NuevaActaEntregaForm.si = si
			NuevaActaEntregaForm.save()

		return redirect("visitas:CRViewActaEntrega", pk=perfil.pk)		