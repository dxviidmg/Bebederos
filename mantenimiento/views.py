from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from accounts.models import Perfil
from django.contrib.auth.models import User
from .models import *
from .forms import *

#Creación y edición de la visita de acuerdo
class ViewMantenimientos(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "mantenimiento/createMantenimiento.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)

		NuevoMantenimientoForm = MantenimientoCreateForm()

		mantenimientos = Mantenimiento.objects.filter(escuela=escuela)

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
		sim = User.objects.get(pk=request.user.pk)

		if NuevoMantenimientoForm.is_valid():
			NuevoMantenimiento = NuevoMantenimientoForm.save(commit=False)
			NuevoMantenimiento.escuela = escuela
			NuevoMantenimiento.sim = sim
			NuevoMantenimiento.save()

		return redirect("mantenimiento:ViewMantenimientos", pk=perfil.pk)