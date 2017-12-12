from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from accounts.models import Perfil
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#Creación y edición de la visita de acuerdo
class CRViewMantenimientos(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "mantenimiento/CRMantenimiento.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		mantenimientos = Mantenimiento.objects.filter(escuela=escuela)
		NuevoMantenimientoForm = MantenimientoCreateForm()
		perfil.UpdateMantenimientosCount()

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'mantenimientos': mantenimientos,
			'NuevoMantenimientoForm': NuevoMantenimientoForm,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)

		NuevoMantenimientoForm = MantenimientoCreateForm(data=request.POST, files=request.FILES)
		if NuevoMantenimientoForm.is_valid():
			NuevoMantenimiento = NuevoMantenimientoForm.save(commit=False)
			NuevoMantenimiento.escuela = escuela
			NuevoMantenimiento.save()

			messages.success(request, "Actualización exitosa")

		return redirect("mantenimiento:CRViewMantenimientos", pk=perfil.pk)

class UpdateViewMantenimiento(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "mantenimiento/updateMantenimiento.html"
		mantenimiento = get_object_or_404(Mantenimiento, pk=pk)
		escuela = User.objects.get(escuela_mtto=mantenimiento)
		perfil = Perfil.objects.get(user=escuela)
		EdicionMantenimientoForm = MantenimientoCreateForm(instance=mantenimiento)
		context = {
			'escuela': escuela,
			'perfil': perfil,			
			'EdicionMantenimientoForm': EdicionMantenimientoForm,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		mantenimiento = get_object_or_404(Mantenimiento, pk=pk)		
		escuela = User.objects.get(escuela_mtto=mantenimiento)
		perfil = Perfil.objects.get(user=escuela)
		EdicionMantenimientoForm = MantenimientoCreateForm(instance=mantenimiento, data=request.POST, files=request.FILES)
		if EdicionMantenimientoForm.is_valid():

			EdicionMantenimientoForm.save()

			messages.success(request, "Actualización exitosa")

		return redirect("mantenimiento:UpdateViewMantenimiento", pk=mantenimiento.pk)