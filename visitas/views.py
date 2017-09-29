from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import *
from django.core.urlresolvers import reverse_lazy
from accounts.models import Perfil
from .forms import *
from django.contrib.auth.models import User

#Creación y edición de la visita de acuerdo
class ViewVisitaDeAcuerdo(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "visitas/createVisitaDeAcuerdo.html"
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

		return redirect("visitas:ViewVisitaDeAcuerdo", pk=perfil.pk)

#Creación y edición de la visita de acuerdo
class ViewEntregaDeBebedero(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "visitas/createEntregaBebedero.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaEntregaForm=EntregaDeBebederoCreateForm()

		try:
			entrega = EntregaDeBebedero.objects.get(escuela=escuela)
		except EntregaDeBebedero.DoesNotExist:
			entrega = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevaEntregaForm': NuevaEntregaForm,
			'entrega': entrega,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaEntregaForm=EntregaDeBebederoCreateForm(data=request.POST, files=request.FILES)
		si = User.objects.get(pk=request.user.pk)

		if NuevaEntregaForm.is_valid():
			NuevaEntrega = NuevaEntregaForm.save(commit=False)
			NuevaEntrega.escuela = escuela
			NuevaEntrega.si = si
			NuevaEntrega.save()

		return redirect("visitas:ViewEntregaDeBebedero", pk=perfil.pk)		