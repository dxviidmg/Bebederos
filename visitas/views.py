from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import *
from django.core.urlresolvers import reverse_lazy
from accounts.models import *
from .forms import *
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#Librerias para generar ZIP
import zipfile
import os
from django.http import HttpResponse
from django.conf import settings
from io import BytesIO

#Creación y consulta de la visita de acuerdo
class CRViewVisitaDeAcuerdo(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "visitas/CRVisitaDeAcuerdo.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaVisitaForm = VisitaDeAcuerdoCreateForm()

		try:
			visita = VisitaDeAcuerdo.objects.get(escuela=escuela)
			EdicionVisitaForm = VisitaDeAcuerdoCreateForm(instance=visita)
		except VisitaDeAcuerdo.DoesNotExist:
			visita = None
			EdicionVisitaForm= None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevaVisitaForm': NuevaVisitaForm,
			'visita': visita,
			'EdicionVisitaForm': EdicionVisitaForm,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevaVisitaForm = VisitaDeAcuerdoCreateForm(data=request.POST, files=request.FILES)

		try:
			visita = VisitaDeAcuerdo.objects.get(escuela=escuela)
			EdicionVisitaForm = VisitaDeAcuerdoCreateForm(instance=visita, files=request.FILES)

			if EdicionVisitaForm.is_valid():
				EdicionVisitaForm.save()
				messages.success(request, "Se cambió el estatus correctamente")	

		except VisitaDeAcuerdo.DoesNotExist:
			visita = None
			EdicionVisitaForm = None

			if NuevaVisitaForm.is_valid():
				NuevaVisita = NuevaVisitaForm.save(commit=False)
				NuevaVisita.escuela = escuela
				NuevaVisita.save()

		return redirect("visitas:CRViewVisitaDeAcuerdo", pk=perfil.pk)

#Creación y consulta de inicio de funcionamiento
class CRViewInicioFuncionamiento(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "visitas/CRInicioFuncionamiento.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevoFuncionamientoForm=InicioFuncionamientoCreateForm()

		try:
			funcionamiento = InicioFuncionamiento.objects.get(escuela=escuela)
			EdicionFuncionamientoForm=InicioFuncionamientoCreateForm(instance=funcionamiento)
		except InicioFuncionamiento.DoesNotExist:
			funcionamiento = None
			EdicionFuncionamientoForm = None
	
		context = {
			'perfil': perfil,
			'escuela': escuela,
			'NuevoFuncionamientoForm': NuevoFuncionamientoForm,
			'funcionamiento': funcionamiento,
			'EdicionFuncionamientoForm': EdicionFuncionamientoForm,
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevoFuncionamientoForm=InicioFuncionamientoCreateForm(data=request.POST, files=request.FILES)

		try:
			funcionamiento = InicioFuncionamiento.objects.get(escuela=escuela)
			EdicionFuncionamientoForm=InicioFuncionamientoCreateForm(instance=funcionamiento, files=request.FILES)

			if EdicionFuncionamientoForm.is_valid():
				EdicionFuncionamientoForm.save()

		except InicioFuncionamiento.DoesNotExist:
			funcionamiento = None
			EdicionFuncionamientoForm = None
			
			if NuevoFuncionamientoForm.is_valid():
				NuevoFuncionamiento = NuevoFuncionamientoForm.save(commit=False)
				NuevoFuncionamiento.escuela = escuela
				NuevoFuncionamiento.save()

		return redirect("visitas:CRViewInicioFuncionamiento", pk=perfil.pk)

#Creación y consulta de Acta de entrega
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

		if NuevaActaEntregaForm.is_valid():
			NuevaActaEntrega = NuevaActaEntregaForm.save(commit=False)
			NuevaActaEntrega.escuela = escuela
			NuevaActaEntregaForm.save()

		return redirect("visitas:CRViewActaEntrega", pk=perfil.pk)

def ExportCedulasIdentificacionZIP(request, pk):
	entidad = get_object_or_404(Entidad, pk=pk)
	zonas = Zona.objects.filter(entidad=entidad)
	municipios = Municipio.objects.filter(zona__in=zonas)
	perfilesEscuelas = Perfil.objects.filter(municipio__in=municipios)
	escuelas = User.objects.filter(perfil__in=perfilesEscuelas)
	visitasAcuerdo = VisitaDeAcuerdo.objects.filter(escuela__in=escuelas)
	origen = settings.BASE_DIR

	filenames = []

	for visitaAcuerdo in visitasAcuerdo:
		cedulaIdentificacion = origen + str(visitaAcuerdo.cedula_identificacion.url)
		filenames.append(cedulaIdentificacion)

	zip_subdir = "Cedulas de identificacion basica de " + str(entidad.nombre)
	zip_filename = "%s.zip" % zip_subdir

	s = BytesIO()
	zf = zipfile.ZipFile(s, "w")

	for fpath in filenames:
		fdir, fname = os.path.split(fpath)
		zip_path = os.path.join(zip_subdir, fname)
		zf.write(fpath, zip_path)

	zf.close()

	response = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
	response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

	return response

def ExportPlanosConjuntoZIP(request, pk):
	entidad = get_object_or_404(Entidad, pk=pk)
	zonas = Zona.objects.filter(entidad=entidad)
	municipios = Municipio.objects.filter(zona__in=zonas)
	perfilesEscuelas = Perfil.objects.filter(municipio__in=municipios)
	escuelas = User.objects.filter(perfil__in=perfilesEscuelas)
	visitasAcuerdo = VisitaDeAcuerdo.objects.filter(escuela__in=escuelas)
	origen = settings.BASE_DIR

	filenames = []

	for visitaAcuerdo in visitasAcuerdo:
		planoConjunto = origen + str(visitaAcuerdo.plano_conjunto.url)
		filenames.append(planoConjunto)

	zip_subdir = "Planos de conjunto de " + str(entidad.nombre)
	zip_filename = "%s.zip" % zip_subdir

	s = BytesIO()
	zf = zipfile.ZipFile(s, "w")

	for fpath in filenames:
		fdir, fname = os.path.split(fpath)
		zip_path = os.path.join(zip_subdir, fname)
		zf.write(fpath, zip_path)

	zf.close()

	response = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
	response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

	return response

def ExportDistribucionesPlantaZIP(request, pk):
	entidad = get_object_or_404(Entidad, pk=pk)
	zonas = Zona.objects.filter(entidad=entidad)
	municipios = Municipio.objects.filter(zona__in=zonas)
	perfilesEscuelas = Perfil.objects.filter(municipio__in=municipios)
	escuelas = User.objects.filter(perfil__in=perfilesEscuelas)
	visitasAcuerdo = VisitaDeAcuerdo.objects.filter(escuela__in=escuelas)
	origen = settings.BASE_DIR

	filenames = []

	for visitaAcuerdo in visitasAcuerdo:
		distribucionPlanta = origen + str(visitaAcuerdo.distribucion_planta.url)
		filenames.append(distribucionPlanta)

	zip_subdir = "Distribuciones de planta de " + str(entidad.nombre)
	zip_filename = "%s.zip" % zip_subdir

	s = BytesIO()
	zf = zipfile.ZipFile(s, "w")

	for fpath in filenames:
		fdir, fname = os.path.split(fpath)
		zip_path = os.path.join(zip_subdir, fname)
		zf.write(fpath, zip_path)

	zf.close()

	response = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
	response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

	return response

def ExportMemoriasCalculoZIP(request, pk):
	entidad = get_object_or_404(Entidad, pk=pk)
	zonas = Zona.objects.filter(entidad=entidad)
	municipios = Municipio.objects.filter(zona__in=zonas)
	perfilesEscuelas = Perfil.objects.filter(municipio__in=municipios)
	escuelas = User.objects.filter(perfil__in=perfilesEscuelas)
	visitasAcuerdo = VisitaDeAcuerdo.objects.filter(escuela__in=escuelas)
	origen = settings.BASE_DIR

	filenames = []

	for visitaAcuerdo in visitasAcuerdo:
		memoriaCalculo = origen + str(visitaAcuerdo.memoria_calculo.url)
		filenames.append(memoriaCalculo)

	zip_subdir = "Memorias de calculo hidrosanitarias y electricas de " + str(entidad.nombre)
	zip_filename = "%s.zip" % zip_subdir

	s = BytesIO()
	zf = zipfile.ZipFile(s, "w")

	for fpath in filenames:
		fdir, fname = os.path.split(fpath)
		zip_path = os.path.join(zip_subdir, fname)
		zf.write(fpath, zip_path)

	zf.close()

	response = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
	response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

	return response

def ExportPlanosInstalacionElectricaZIP(request, pk):
	entidad = get_object_or_404(Entidad, pk=pk)
	zonas = Zona.objects.filter(entidad=entidad)
	municipios = Municipio.objects.filter(zona__in=zonas)
	perfilesEscuelas = Perfil.objects.filter(municipio__in=municipios)
	escuelas = User.objects.filter(perfil__in=perfilesEscuelas)
	visitasAcuerdo = VisitaDeAcuerdo.objects.filter(escuela__in=escuelas)
	origen = settings.BASE_DIR

	filenames = []

	for visitaAcuerdo in visitasAcuerdo:
		planoInstalacionElectrica = origen + str(visitaAcuerdo.plano_instalacion_electrica.url)
		filenames.append(planoInstalacionElectrica)

	zip_subdir = "Planos de instalaciones electricas de " + str(entidad.nombre)
	zip_filename = "%s.zip" % zip_subdir

	s = BytesIO()
	zf = zipfile.ZipFile(s, "w")

	for fpath in filenames:
		fdir, fname = os.path.split(fpath)
		zip_path = os.path.join(zip_subdir, fname)
		zf.write(fpath, zip_path)

	zf.close()

	response = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
	response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

	return response	

def ExportPlanosInstalacionHidraculicaZIP(request, pk):
	entidad = get_object_or_404(Entidad, pk=pk)
	zonas = Zona.objects.filter(entidad=entidad)
	municipios = Municipio.objects.filter(zona__in=zonas)
	perfilesEscuelas = Perfil.objects.filter(municipio__in=municipios)
	escuelas = User.objects.filter(perfil__in=perfilesEscuelas)
	visitasAcuerdo = VisitaDeAcuerdo.objects.filter(escuela__in=escuelas)
	origen = settings.BASE_DIR

	filenames = []

	for visitaAcuerdo in visitasAcuerdo:
		planoInstalacionHidraulica = origen + str(visitaAcuerdo.plano_instalacion_hidraulica.url)
		filenames.append(planoInstalacionHidraulica)

	zip_subdir = "Planos de instalaciones hidraulicas de " + str(entidad.nombre)
	zip_filename = "%s.zip" % zip_subdir

	s = BytesIO()
	zf = zipfile.ZipFile(s, "w")

	for fpath in filenames:
		fdir, fname = os.path.split(fpath)
		zip_path = os.path.join(zip_subdir, fname)
		zf.write(fpath, zip_path)

	zf.close()

	response = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
	response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

	return response	

def ExportPlanosInstalacionSanitariaZIP(request, pk):
	entidad = get_object_or_404(Entidad, pk=pk)
	zonas = Zona.objects.filter(entidad=entidad)
	municipios = Municipio.objects.filter(zona__in=zonas)
	perfilesEscuelas = Perfil.objects.filter(municipio__in=municipios)
	escuelas = User.objects.filter(perfil__in=perfilesEscuelas)
	visitasAcuerdo = VisitaDeAcuerdo.objects.filter(escuela__in=escuelas)
	origen = settings.BASE_DIR

	filenames = []

	for visitaAcuerdo in visitasAcuerdo:
		planoInstalacionSanitaria = origen + str(visitaAcuerdo.plano_instalacion_sanitaria.url)
		filenames.append(planoInstalacionSanitaria)

	zip_subdir = "Planos de instalaciones sanitarias de " + str(entidad.nombre)
	zip_filename = "%s.zip" % zip_subdir

	s = BytesIO()
	zf = zipfile.ZipFile(s, "w")

	for fpath in filenames:
		fdir, fname = os.path.split(fpath)
		zip_path = os.path.join(zip_subdir, fname)
		zf.write(fpath, zip_path)

	zf.close()

	response = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
	response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

	return response

def ExportActasFuncionamietoZIP(request, pk):
	entidad = get_object_or_404(Entidad, pk=pk)
	zonas = Zona.objects.filter(entidad=entidad)
	municipios = Municipio.objects.filter(zona__in=zonas)
	perfilesEscuelas = Perfil.objects.filter(municipio__in=municipios)
	escuelas = User.objects.filter(perfil__in=perfilesEscuelas)
	iniciosFuncionamiento = InicioFuncionamiento.objects.filter(escuela__in=escuelas)
	origen = settings.BASE_DIR

	filenames = []

	for inicioFuncionamiento in iniciosFuncionamiento:
		actaFuncionamiento = origen + str(inicioFuncionamiento.acta_funcionamiento.url)
		filenames.append(actaFuncionamiento)

	zip_subdir = "Actas de inicio de funcionamiento de " + str(entidad.nombre)
	zip_filename = "%s.zip" % zip_subdir

	s = BytesIO()
	zf = zipfile.ZipFile(s, "w")

	for fpath in filenames:
		fdir, fname = os.path.split(fpath)
		zip_path = os.path.join(zip_subdir, fname)
		zf.write(fpath, zip_path)

	zf.close()

	response = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
	response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

	return response