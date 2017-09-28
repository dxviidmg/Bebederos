from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import *
from accounts.models import Perfil
from .forms import *
from accounts.models import *
from django.utils.timezone import datetime

#Creación y edición de la visita de acuerdo
class ViewBebederos(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "bebederos/createBebedero.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		municipio = Municipio.objects.get(perfil=perfil)
		zona = Zona.objects.get(municipio=municipio)
		entidad = Entidad.objects.get(zona=zona)
		zona = Zona.objects.get(municipio=municipio)
		entidad = Entidad.objects.get(zona=zona)
		countSB = SistemaBebedero.objects.all().count()
 
		NuevoBebederoForm = BebederoCreateForm()

		try:
			sistemaBebedero = SistemaBebedero.objects.get(escuela=escuela)
			EdicionBebederoForm = BebederoEditForm(instance=sistemaBebedero)

			if entidad.abreviatura and sistemaBebedero.mueble and sistemaBebedero.sistema_de_potabilizacion and sistemaBebedero.linea_ensamblaje:
				GeneraNSBebederoForm = BebederoGeneraNSForm(instance=sistemaBebedero)
				cantidadCeros = 4-len(str(countSB))
				serie = cantidadCeros*"0" + str(countSB)
				hoy = datetime.today().strftime('%d%m%y')
				no_serie = str(entidad.abreviatura) + str(sistemaBebedero.mueble) + str(sistemaBebedero.sistema_de_potabilizacion) + str(serie) + str(hoy) + "T304" + str(sistemaBebedero.linea_ensamblaje) + str(escuela.username)
				print(no_serie)

		except SistemaBebedero.DoesNotExist:
			sistemaBebedero = None
			EdicionBebederoForm = None
			GeneraNSBebederoForm = None



		context = {
			'perfil': perfil,
			'escuela': escuela,
			'sistemaBebedero': sistemaBebedero,
			'EdicionBebederoForm': EdicionBebederoForm,
			'NuevoBebederoForm': NuevoBebederoForm,
			'GeneraNSBebederoForm': GeneraNSBebederoForm
		}
		return render(request, template_name, context)

	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)

		NuevoBebederoForm = BebederoCreateForm(data=request.POST, files=request.FILES)
		si = User.objects.get(pk=request.user.pk)

		if NuevoBebederoForm.is_valid():
			NuevoBebedero = NuevoBebederoForm.save(commit=False)
			NuevoBebedero.escuela = escuela
			NuevoBebedero.si = si
			NuevoBebedero.save()

		try:
			bebedero = SistemaBebedero.objects.get(escuela=escuela)
			if bebedero:

				GeneraNSBebederoForm = BebederoGeneraNSForm(instance=bebedero, data=request.POST, files=request.FILES)

				if GeneraNSBebederoForm.is_valid():


					municipio = Municipio.objects.get(perfil=perfil)
					zona = Zona.objects.get(municipio=municipio)
					entidad = Entidad.objects.get(zona=zona)
					zona = Zona.objects.get(municipio=municipio)
					entidad = Entidad.objects.get(zona=zona)
					countSB = SistemaBebedero.objects.all().count()
					countSB = SistemaBebedero.objects.all().count()
					sistemaBebedero = SistemaBebedero.objects.get(escuela=escuela)

					GeneraNSBebederoForm = BebederoGeneraNSForm(instance=sistemaBebedero)
					cantidadCeros = 4-len(str(countSB))
					serie = cantidadCeros*"0" + str(countSB)
					hoy = datetime.today().strftime('%d%m%y')
					no_serie = str(entidad.abreviatura) + str(sistemaBebedero.mueble) + str(sistemaBebedero.sistema_de_potabilizacion) + str(serie) + str(hoy) + "T304" + str(sistemaBebedero.linea_ensamblaje) + str(escuela.username)



					GeneraNSBebedero = GeneraNSBebederoForm.save(commit=False)
					GeneraNSBebedero.no_serie = no_serie
					GeneraNSBebedero.save()	
		except SistemaBebedero.DoesNotExist:
			bebedero = None

		return redirect("bebederos:ViewBebederos", pk=perfil.pk)		