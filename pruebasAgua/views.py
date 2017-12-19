from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from accounts.models import *
from django.contrib.auth.models import User
from .forms import *
from django.http import HttpResponse
import csv
from django_modalview.generic.base import ModalTemplateView
from bebederos.forms import BebederoUpdateForm5
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#Creación, edición y detalle de una Primer Prueba
class CRUViewPrimerPrueba(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "pruebasAgua/CRUPrimerPrueba.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaPruebaForm = PrimerPruebaCreateForm()
		sistemaBebedero = SistemaBebedero.objects.get(escuela=escuela)
		EdicionBebederoForm = BebederoUpdateForm5(instance=sistemaBebedero)		
		sistemaPotabilizadorCalculado = None		
	
		try:
			prueba = PrimerPrueba.objects.get(escuela=escuela)
			EdicionPruebaForm0 = PrimerPruebaCreateForm(instance=prueba)
			EdicionPruebaForm1 = PrimerPruebaUpdateForm1(instance=prueba)
			EdicionPruebaForm2 = PrimerPruebaUpdateForm2(instance=prueba)
			EdicionPruebaForm3 = PrimerPruebaUpdateForm3(instance=prueba)
			EdicionPruebaForm4 = PrimerPruebaUpdateForm4(instance=prueba)
			EdicionPruebaForm5 = PrimerPruebaUpdateForm5(instance=prueba)
			EdicionPruebaForm6 = PrimerPruebaUpdateForm6(instance=prueba)
			EdicionPruebaForm7 = PrimerPruebaUpdateForm7(instance=prueba)
			EdicionPruebaForm8 = PrimerPruebaUpdateForm8(instance=prueba)
			EdicionPruebaForm9 = PrimerPruebaUpdateForm9(instance=prueba)
			EdicionPruebaForm10 = PrimerPruebaUpdateForm10(instance=prueba)
			EdicionPruebaForm11 = PrimerPruebaUpdateForm11(instance=prueba)
			EdicionPruebaForm12 = PrimerPruebaUpdateForm12(instance=prueba)

			color_verdadero = prueba.color_verdadero
			turbiedad = prueba.turbiedad
			ph = prueba.ph
			conductividad_electrica = prueba.conductividad_electrica
			coliformes_fecales = prueba.coliformes_fecales
			coliformes_totales = prueba.coliformes_totales
			arsenico = prueba.arsenico
			hierro = prueba.hierro
			manganeso = prueba.manganeso
			plomo = prueba.plomo
			floururos = prueba.floururos
			nitratos = prueba.nitratos
			sulfatos = prueba.sulfatos
			dureza_total = prueba.dureza_total
			solidos_disueltos  = prueba.solidos_disueltos

			if manganeso is not None:
				if manganeso > 0.165 or plomo > 0.011 or floururos > 0.7:
					sistemaPotabilizadorCalculado = "Robusto"
				elif arsenico > 0.0275 or hierro > 0.2 or nitratos > 11 or sulfatos > 440:
					sistemaPotabilizadorCalculado = "Intermedio"
				else:
					 sistemaPotabilizadorCalculado = "Basico"

		except PrimerPrueba.DoesNotExist:
			prueba = None
			EdicionPruebaForm0 = None
			EdicionPruebaForm1 = None
			EdicionPruebaForm2 = None
			EdicionPruebaForm3 = None
			EdicionPruebaForm4 = None
			EdicionPruebaForm5 = None
			EdicionPruebaForm6 = None
			EdicionPruebaForm7 = None
			EdicionPruebaForm8 = None
			EdicionPruebaForm9 = None
			EdicionPruebaForm10 = None
			EdicionPruebaForm11 = None
			EdicionPruebaForm12 = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevaPruebaForm': NuevaPruebaForm,
			'prueba': prueba,
			'EdicionPruebaForm0': EdicionPruebaForm0,
			'EdicionPruebaForm1': EdicionPruebaForm1,
			'EdicionPruebaForm2': EdicionPruebaForm2,
			'EdicionPruebaForm8': EdicionPruebaForm8,
			'EdicionPruebaForm3': EdicionPruebaForm3,
			'EdicionPruebaForm4': EdicionPruebaForm4,
			'EdicionPruebaForm5': EdicionPruebaForm5,
			'EdicionPruebaForm6': EdicionPruebaForm6,
			'EdicionPruebaForm7': EdicionPruebaForm7,
			'EdicionPruebaForm8': EdicionPruebaForm8,
			'EdicionPruebaForm9': EdicionPruebaForm9,
			'EdicionPruebaForm10': EdicionPruebaForm10,
			'EdicionPruebaForm11': EdicionPruebaForm11,
			'EdicionPruebaForm12': EdicionPruebaForm12,
			'sistemaPotabilizadorCalculado': sistemaPotabilizadorCalculado,
			'EdicionBebederoForm': EdicionBebederoForm,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaPruebaForm = PrimerPruebaCreateForm(data=request.POST, files=request.FILES)
		laboratorio = User.objects.get(pk=request.user.pk)
		sistemaBebedero = SistemaBebedero.objects.get(escuela=escuela)
		EdicionBebederoForm = BebederoUpdateForm5(instance=sistemaBebedero, data=request.POST, files=request.FILES)

		try:
			prueba = PrimerPrueba.objects.get(escuela=escuela)
			EdicionPruebaForm0 = PrimerPruebaCreateForm(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm1 = PrimerPruebaUpdateForm1(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm2 = PrimerPruebaUpdateForm2(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm3 = PrimerPruebaUpdateForm3(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm4 = PrimerPruebaUpdateForm4(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm5 = PrimerPruebaUpdateForm5(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm6 = PrimerPruebaUpdateForm6(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm7 = PrimerPruebaUpdateForm7(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm8 = PrimerPruebaUpdateForm8(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm9 = PrimerPruebaUpdateForm9(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm10 = PrimerPruebaUpdateForm10(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm11 = PrimerPruebaUpdateForm11(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm12 = PrimerPruebaUpdateForm12(instance=prueba, data=request.POST, files=request.FILES)

			if EdicionPruebaForm0.is_valid():
				EdicionPruebaForm0.save()

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

			if EdicionPruebaForm8.is_valid():
				EdicionPruebaForm8.save()

			if EdicionPruebaForm9.is_valid():
				EdicionPruebaForm9.save()

			if EdicionPruebaForm10.is_valid():
				EdicionPruebaForm10.save()

			if EdicionPruebaForm11.is_valid():
				EdicionPruebaForm11.save()

			if EdicionPruebaForm12.is_valid():
				EdicionPruebaForm12.save()
		except PrimerPrueba.DoesNotExist:
			prueba = None
			EdicionPruebaForm0 = None
			EdicionPruebaForm1 = None
			EdicionPruebaForm2 = None
			EdicionPruebaForm3 = None
			EdicionPruebaForm4 = None
			EdicionPruebaForm5 = None
			EdicionPruebaForm6 = None
			EdicionPruebaForm7 = None
			EdicionPruebaForm8 = None
			EdicionPruebaForm9 = None
			EdicionPruebaForm10 = None
			EdicionPruebaForm11 = None
			EdicionPruebaForm12 = None

			if NuevaPruebaForm.is_valid():
				NuevaPrueba = NuevaPruebaForm.save(commit=False)
				NuevaPrueba.escuela = escuela
				NuevaPrueba.laboratorio = laboratorio
				NuevaPrueba.save()

			if EdicionBebederoForm.is_valid():
				EdicionBebederoForm.save()
			
		return redirect("pruebas:CRUViewPrimerPrueba", pk=perfil.pk)

#Creación, edición y detalle de una Segunda prueba
class CRUViewSegundaPrueba(View):
	@method_decorator(login_required)
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
			EdicionPruebaForm4 = SegundaPruebaUpdateForm4(instance=prueba)
			EdicionPruebaForm5 = SegundaPruebaUpdateForm5(instance=prueba)
			EdicionPruebaForm6 = SegundaPruebaUpdateForm6(instance=prueba)
			EdicionPruebaForm7 = SegundaPruebaUpdateForm7(instance=prueba)
			EdicionPruebaForm8 = SegundaPruebaUpdateForm8(instance=prueba)
			EdicionPruebaForm9 = SegundaPruebaUpdateForm9(instance=prueba)
			EdicionPruebaForm10 = SegundaPruebaUpdateForm10(instance=prueba)
			EdicionPruebaForm11 = SegundaPruebaUpdateForm11(instance=prueba)
			EdicionPruebaForm12 = SegundaPruebaUpdateForm12(instance=prueba)

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
			EdicionPruebaForm8 = None
			EdicionPruebaForm9 = None
			EdicionPruebaForm10 = None
			EdicionPruebaForm11 = None
			EdicionPruebaForm12 = None

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
			'EdicionPruebaForm8': EdicionPruebaForm8,
			'EdicionPruebaForm9': EdicionPruebaForm9,
			'EdicionPruebaForm10': EdicionPruebaForm10,
			'EdicionPruebaForm11': EdicionPruebaForm11,
			'EdicionPruebaForm12': EdicionPruebaForm12,			
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
			EdicionPruebaForm4 = SegundaPruebaUpdateForm4(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm5 = SegundaPruebaUpdateForm5(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm6 = SegundaPruebaUpdateForm6(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm7 = SegundaPruebaUpdateForm7(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm8 = SegundaPruebaUpdateForm8(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm9 = SegundaPruebaUpdateForm9(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm10 = SegundaPruebaUpdateForm10(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm11 = SegundaPruebaUpdateForm11(instance=prueba, data=request.POST, files=request.FILES)
			EdicionPruebaForm12 = SegundaPruebaUpdateForm12(instance=prueba, data=request.POST, files=request.FILES)

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

			if EdicionPruebaForm8.is_valid():
				EdicionPruebaForm8.save()

			if EdicionPruebaForm9.is_valid():
				EdicionPruebaForm9.save()

			if EdicionPruebaForm10.is_valid():
				EdicionPruebaForm10.save()

			if EdicionPruebaForm11.is_valid():
				EdicionPruebaForm11.save()

			if EdicionPruebaForm12.is_valid():
				EdicionPruebaForm12.save()				

		except SegundaPrueba.DoesNotExist:
			prueba = None
			EdicionPruebaForm1 = None
			EdicionPruebaForm2 = None
			EdicionPruebaForm3 = None
			EdicionPruebaForm4 = None
			EdicionPruebaForm5 = None
			EdicionPruebaForm6 = None
			EdicionPruebaForm7 = None
			EdicionPruebaForm8 = None
			EdicionPruebaForm9 = None
			EdicionPruebaForm10 = None
			EdicionPruebaForm11 = None
			EdicionPruebaForm12 = None

		return redirect("pruebas:CRUViewSegundaPrueba", pk=perfil.pk)

def ExportPruebasPorEscuelasCSV(request, pk):
	entidad = get_object_or_404(Entidad, pk=pk)
	zonas = Zona.objects.filter(entidad=entidad)
	municipios=Municipio.objects.filter(zona__in=zonas)
	perfiles = Perfil.objects.filter(municipio__in=municipios)
	escuelas = User.objects.filter(perfil__in=perfiles).values_list('perfil__municipio__zona__entidad__laboratorio__first_name', 'escuela_primer_prueba__no_registro', 'username', 'first_name','perfil__municipio__nombre', 'perfil__localidad', 'perfil__domicilio', 'perfil__nivel_educativo', 'perfil__plantilla_escolar', 'escuela__mueble__salidas_regulares', 'escuela__mueble__salidas_discapacidad', 'escuela__mueble__llenador_botellas', 'escuela__mueble__total_salidas', 'escuela__mueble__modelo', 'escuela_primer_prueba__creacion', 'escuela_primer_prueba__creacion_reporte_analisis', 'escuela_primer_prueba__color_verdadero', 'escuela_primer_prueba__turbiedad', 'escuela_primer_prueba__ph', 'escuela_primer_prueba__conductividad_electrica', 'escuela_primer_prueba__coliformes_fecales', 'escuela_primer_prueba__coliformes_totales', 'escuela_primer_prueba__arsenico',  'escuela_primer_prueba__hierro',  'escuela_primer_prueba__manganeso', 'escuela_primer_prueba__plomo', 'escuela_primer_prueba__floururos', 'escuela_primer_prueba__nitratos', 'escuela_primer_prueba__sulfatos', 'escuela_primer_prueba__dureza_total','escuela_primer_prueba__solidos_disueltos', 'escuela__sistema_potabilizacion__tipo', 'escuela_primer_prueba__validacion', 'escuela_segunda_prueba__creacion', 'escuela_segunda_prueba__creacion_reporte_analisis', 'escuela_segunda_prueba__color_verdadero', 'escuela_segunda_prueba__turbiedad', 'escuela_segunda_prueba__ph', 'escuela_segunda_prueba__conductividad_electrica', 'escuela_segunda_prueba__coliformes_fecales', 'escuela_segunda_prueba__coliformes_totales', 'escuela_segunda_prueba__arsenico',  'escuela_segunda_prueba__hierro',  'escuela_segunda_prueba__manganeso', 'escuela_segunda_prueba__plomo', 'escuela_segunda_prueba__floururos', 'escuela_segunda_prueba__nitratos', 'escuela_segunda_prueba__sulfatos', 'escuela_segunda_prueba__dureza_total','escuela_segunda_prueba__solidos_disueltos', 'escuela_segunda_prueba__validacion', 'escuela__no_trazabilidad')

	ahora = datetime.now().strftime("%d-%m-%Y %H:%M")

	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="Base de formato T7 de '+ entidad.nombre + ' ' + ahora + '.csv"'
	writer = csv.writer(response)
	writer.writerow(['Laboratorio', 'No. de registro','C. C. T.','Nombre del plantel', 'Municipio', 'Localidad', 'Domicilio', 'Nivel Educativo', 'Plantilla escolar', 'Boquillas regulares', 'Boquilla para discapacitados', 'Llave de llenado para botella', 'Total de salidas', 'Tipo de bebedero', 'Fecha de muestreo', 'Fecha de reporte de análisis', 'Color verdadero (U PT-Co)', 'Turbiedad (UTN o equivalente)', 'pH (unidades de pH)', 'Conductividad eléctrica (µS/cm)', 'Coliformes fecales (Unidades)', 'Coliformes totales (Unidades)', 'Arsénico', 'Hierro', 'Manganeso', 'Plomo', 'Floururos', 'Nitratos', 'Sulfatos', 'Dureza total (CaCO3)', 'Sólidos disueltos totales', 'Equipo de potabilización', 'Validación IMTA', 'Fecha de muestreo', 'Fecha de reporte de análisis', 'Color verdadero (U Pt-Co)', 'Turbiedad (UTN o equivalente)', 'pH (unidades de pH)', 'Conductividad eléctrica (µS/cm)', 'Coliformes fecales (Unidades)', 'Coliformes totales (Unidades)', 'Arsénico', 'Hierro', 'Manganeso', 'Plomo', 'Floururos', 'Nitratos', 'Sulfatos', 'Dureza total (CaCO3)', 'Sólidos disueltos totales', 'Validación IMTA', 'Guía de trazabilidad'])

	for escuela in escuelas:
		writer.writerow(escuela)

	return response