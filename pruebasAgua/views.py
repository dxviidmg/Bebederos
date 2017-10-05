from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from accounts.models import Perfil
from django.contrib.auth.models import User
from .forms import *

class CRUViewPrimerPrueba(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "pruebasAgua/CRUPrimerPrueba.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaPruebaForm = PrimerPruebaCreateForm()

		try:
			prueba = PrimerPrueba.objects.get(escuela=escuela)
			EdicionPruebaForm1 = PrimerPruebaUpdateForm1(instance=prueba)
			EdicionPruebaForm2 = PrimerPruebaUpdateForm2(instance=prueba)
			EdicionPruebaForm3 = PrimerPruebaUpdateForm3(instance=prueba)
			EdicionPruebaForm4 = PrimerPruebaUpdateForm4(instance=prueba)
			EdicionPruebaForm5 = PrimerPruebaUpdateForm5(instance=prueba)
			EdicionPruebaForm6 = PrimerPruebaUpdateForm6(instance=prueba)
			EdicionPruebaForm7 = PrimerPruebaUpdateForm7(instance=prueba)

		except PrimerPrueba.DoesNotExist:
			prueba = None
			EdicionPruebaForm1 = None
			EdicionPruebaForm2 = None
			EdicionPruebaForm3 = None
			EdicionPruebaForm4 = None
			EdicionPruebaForm5 = None
			EdicionPruebaForm6 = None
			EdicionPruebaForm7 = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevaPruebaForm': NuevaPruebaForm,
			'prueba': prueba,
			'EdicionPruebaForm1': EdicionPruebaForm1,
			'EdicionPruebaForm2': EdicionPruebaForm2,
			'EdicionPruebaForm3': EdicionPruebaForm3,
			'EdicionPruebaForm4': EdicionPruebaForm4,
			'EdicionPruebaForm5': EdicionPruebaForm5,
			'EdicionPruebaForm6': EdicionPruebaForm6,
			'EdicionPruebaForm7': EdicionPruebaForm7,
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
			EdicionPruebaForm4 = PrimerPruebaUpdateForm4(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm5 = PrimerPruebaUpdateForm5(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm6 = PrimerPruebaUpdateForm6(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm7 = PrimerPruebaUpdateForm7(instance=prueba, data=request.POST, files=request.FILES)

			if EdicionPruebaForm1.is_valid():
				EdicionPruebaForm1.save()

			if EdicionPruebaForm2.is_valid():
				EdicionPruebaForm2.save()

			if EdicionPruebaForm3.is_valid():
				EdicionPruebaForm3.save()

			if EdicionPruebaForm4.is_valid():
				EdicionPruebaForm4.save()

			if EdicionPruebaForm5.is_valid():
				EdicionPruebaForm5.save()

			if EdicionPruebaForm6.is_valid():
				EdicionPruebaForm6.save()

			if EdicionPruebaForm7.is_valid():
				EdicionPruebaForm7.save()

		except PrimerPrueba.DoesNotExist:
			prueba = None
			EdicionPruebaForm1 = None
			EdicionPruebaForm2 = None
			EdicionPruebaForm3 = None
			EdicionPruebaForm4 = None
			EdicionPruebaForm5 = None
			EdicionPruebaForm6 = None
			EdicionPruebaForm7 = None

		return redirect("pruebas:CRUViewPrimerPrueba", pk=perfil.pk)

class CRUViewSegundaPrueba(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "pruebasAgua/CRUSegundaPrueba.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaPruebaForm = SegundaPruebaCreateForm()

		try:
			prueba = SegundaPrueba.objects.get(escuela=escuela)
			EdicionPruebaForm0 = SegundaPruebaCreateForm(instance=prueba)
			EdicionPruebaForm1 = SegundaPruebaUpdateForm1(instance=prueba)
			EdicionPruebaForm2 = SegundaPruebaUpdateForm2(instance=prueba)
			EdicionPruebaForm3 = SegundaPruebaUpdateForm3(instance=prueba)
			EdicionPruebaForm4 = PrimerPruebaUpdateForm4(instance=prueba)
			EdicionPruebaForm5 = PrimerPruebaUpdateForm5(instance=prueba)
			EdicionPruebaForm6 = PrimerPruebaUpdateForm6(instance=prueba)
			EdicionPruebaForm7 = PrimerPruebaUpdateForm7(instance=prueba)

		except SegundaPrueba.DoesNotExist:
			prueba = None
			EdicionPruebaForm0 = None
			EdicionPruebaForm1 = None
			EdicionPruebaForm2 = None
			EdicionPruebaForm3 = None
			EdicionPruebaForm4 = None
			EdicionPruebaForm5 = None
			EdicionPruebaForm6 = None
			EdicionPruebaForm7 = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevaPruebaForm': NuevaPruebaForm,
			'prueba': prueba,
			'EdicionPruebaForm0': EdicionPruebaForm0,
			'EdicionPruebaForm1': EdicionPruebaForm1,
			'EdicionPruebaForm2': EdicionPruebaForm2,
			'EdicionPruebaForm3': EdicionPruebaForm3,
			'EdicionPruebaForm4': EdicionPruebaForm4,
			'EdicionPruebaForm5': EdicionPruebaForm5,
			'EdicionPruebaForm6': EdicionPruebaForm6,
			'EdicionPruebaForm7': EdicionPruebaForm7,
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
			EdicionPruebaForm1 = SegundaPruebaUpdateForm1(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm2 = SegundaPruebaUpdateForm2(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm3 = SegundaPruebaUpdateForm3(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm4 = PrimerPruebaUpdateForm4(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm5 = PrimerPruebaUpdateForm5(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm6 = PrimerPruebaUpdateForm6(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm7 = PrimerPruebaUpdateForm7(instance=prueba, data=request.POST, files=request.FILES)			

			if EdicionPruebaForm1.is_valid():
				EdicionPruebaForm1.save()

			if EdicionPruebaForm2.is_valid():
				EdicionPruebaForm2.save()

			if EdicionPruebaForm3.is_valid():
				EdicionPruebaForm3.save()

			if EdicionPruebaForm4.is_valid():
				EdicionPruebaForm4.save()

			if EdicionPruebaForm5.is_valid():
				EdicionPruebaForm5.save()

			if EdicionPruebaForm6.is_valid():
				EdicionPruebaForm6.save()

			if EdicionPruebaForm7.is_valid():
				EdicionPruebaForm7.save()

		except SegundaPrueba.DoesNotExist:
			prueba = None
			EdicionPruebaForm1 = None
			EdicionPruebaForm2 = None
			EdicionPruebaForm3 = None
			EdicionPruebaForm4 = None
			EdicionPruebaForm5 = None
			EdicionPruebaForm6 = None
			EdicionPruebaForm7 = None

		return redirect("pruebas:CRUViewSegundaPrueba", pk=perfil.pk)