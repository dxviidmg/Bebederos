from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from accounts.models import Perfil
from django.contrib.auth.models import User
from .forms import *

class ViewPrimerPrueba(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "pruebasAgua/createPrimerPrueba.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaPruebaForm = PrimerPruebaCreateForm()

		try:
			prueba = PrimerPrueba.objects.get(escuela=escuela)
			EdicionPruebaForm1 = PrimerPruebaUpdateForm1(instance=prueba)
			EdicionPruebaForm2 = PrimerPruebaUpdateForm2(instance=prueba)
			EdicionPruebaForm3 = PrimerPruebaUpdateForm3(instance=prueba)
		except PrimerPrueba.DoesNotExist:
			prueba = None
		
		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevaPruebaForm': NuevaPruebaForm,
			'prueba': prueba,
			'EdicionPruebaForm1': EdicionPruebaForm1,
			'EdicionPruebaForm2': EdicionPruebaForm2,
			'EdicionPruebaForm3': EdicionPruebaForm3,			
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaPruebaForm = PrimerPruebaCreateForm(data=request.POST, files=request.FILES)
		laboratorio = User.objects.get(pk=request.user.pk)

		if NuevaPruebaForm.is_valid():
			NuevaPrueba = NuevaPruebaForm.save(commit=False)
			NuevaPrueba.escuela = escuela
			NuevaPrueba.laboratorio = laboratorio
			NuevaPrueba.save()

		try:
			prueba = PrimerPrueba.objects.get(escuela=escuela)
			EdicionPruebaForm1 = PrimerPruebaUpdateForm1(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm2 = PrimerPruebaUpdateForm2(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm3 = PrimerPruebaUpdateForm3(instance=prueba, data=request.POST, files=request.FILES)
			
			if EdicionPruebaForm1.is_valid():
				EdicionPruebaForm1.save()

			if EdicionPruebaForm2.is_valid():
				EdicionPruebaForm2.save()

			if EdicionPruebaForm3.is_valid():
				EdicionPruebaForm3.save()

		except PrimerPrueba.DoesNotExist:
			prueba = None
			EdicionPruebaForm1 = None
			EdicionPruebaForm2 = None

		return redirect("pruebas:ViewPrimerPrueba", pk=perfil.pk)

class ViewSegundaPrueba(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "pruebasAgua/createSegundaPrueba.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaPruebaForm = SegundaPruebaCreateForm()

		try:
			prueba = SegundaPrueba.objects.get(escuela=escuela)
			EdicionPruebaForm = SegundaPruebaEditForm(instance=prueba)
		except SegundaPrueba.DoesNotExist:
			prueba = None
			EdicionPruebaForm = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevaPruebaForm': NuevaPruebaForm,
			'prueba': prueba,
			'EdicionPruebaForm': EdicionPruebaForm
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaPruebaForm = SegundaPruebaCreateForm(data=request.POST, files=request.FILES)
		laboratorio = User.objects.get(pk=request.user.pk)

		if NuevaPruebaForm.is_valid():
			NuevaPrueba = NuevaPruebaForm.save(commit=False)
			NuevaPrueba.escuela = escuela
			NuevaPrueba.laboratorio = laboratorio
			NuevaPrueba.save()

		try:
			prueba = SegundaPrueba.objects.get(escuela=escuela)
			EdicionPruebaForm = SegundaPruebaEditForm(instance=prueba, data=request.POST, files=request.FILES)

			if EdicionPruebaForm.is_valid():
				EdicionPruebaForm.save()

		except SegundaPrueba.DoesNotExist:
			prueba = None
			EdicionPruebaForm = None

		return redirect("pruebas:ViewSegundaPrueba", pk=perfil.pk)