from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import *
from accounts.models import Perfil
from .forms import *
from accounts.models import *
from django.utils.timezone import datetime

#Actualización de un SistemasBebedero
class UpdateViewBebedero(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "bebederos/createBebedero.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		municipio = Municipio.objects.get(perfil=perfil)
		zona = Zona.objects.get(municipio=municipio)
		entidad = Entidad.objects.get(zona=zona)
		countSB = SistemaBebedero.objects.all().count()
 
		sistemaBebedero = SistemaBebedero.objects.get(escuela=escuela)
		EdicionBebederoForm = BebederoEditForm(instance=sistemaBebedero)

		GeneraNSBebederoForm = BebederoGeneraNSForm(instance=sistemaBebedero)

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'entidad': entidad,
			'sistemaBebedero': sistemaBebedero,
			'EdicionBebederoForm': EdicionBebederoForm,
			'GeneraNSBebederoForm': GeneraNSBebederoForm
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		municipio = Municipio.objects.get(perfil=perfil)
		zona = Zona.objects.get(municipio=municipio)
		entidad = Entidad.objects.get(zona=zona)
		zona = Zona.objects.get(municipio=municipio)
		entidad = Entidad.objects.get(zona=zona)
		countSB = SistemaBebedero.objects.all().count()
		sistemaBebedero = SistemaBebedero.objects.get(escuela=escuela)

		EdicionBebederoForm = BebederoEditForm(instance=sistemaBebedero, data=request.POST)
		if EdicionBebederoForm.is_valid():
			EdicionBebederoForm.save()

		cantidadCeros = 4-len(str(countSB))
		serie = cantidadCeros*"0" + str(countSB)
		hoy = datetime.today().strftime('%d%m%y')
		identificador = str(entidad.abreviatura) + str(sistemaBebedero.mueble) + str(sistemaBebedero.sistema_de_potabilizacion) + str(serie) + str(hoy) + "T304" + str(sistemaBebedero.linea_ensamblaje) + str(escuela.username)

		GeneraNSBebederoForm = BebederoGeneraNSForm(instance=sistemaBebedero, data=request.POST)
		if GeneraNSBebederoForm.is_valid():
			GeneraNSBebedero = GeneraNSBebederoForm.save(commit=False)
			GeneraNSBebedero.identificador = identificador
			GeneraNSBebedero.save()

		return redirect("bebederos:UpdateViewBebedero", pk=perfil.pk)		