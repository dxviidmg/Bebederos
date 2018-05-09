from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import *
from visitas.models import *
from construccion.models import *
from pruebasAgua.models import *
from bebederos.models import *
from mantenimiento.models import Mantenimiento
from .forms import *
from bebederos.forms import BebederoCreateForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import csv
from datetime import datetime

#Librerias para generar ZIP
import zipfile
import os
from django.http import HttpResponse
from django.conf import settings
from io import BytesIO

#Ver perfil al iniciar sesión
class ViewProfile(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/profile.html"
		user = User.objects.get(pk=request.user.pk)

		try:
			perfil = Perfil.objects.get(user=user)
			entidad = Entidad.objects.get(coordinador_estatal=user)
		except:
			perfil = None
	
		context = {
			'perfil': perfil,
		}
		return render(request,template_name, context)

#Lista de regiones
class ListViewRegiones(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/listRegiones.html"	
		user = User.objects.get(pk=request.user.pk)
		perfil = Perfil.objects.get(user=user)

		regiones = Region.objects.all()

		context = {
			'regiones': regiones,
		}
		return render(request,template_name, context)

#Lista de entidades
class ListViewEntidades(View):
	@method_decorator(login_required)
	def get(self, request, numero=None):
		template_name = "accounts/listEntidades.html"
		
		if request.user.perfil.cargo == "SIM":
			region = None
			sim = User.objects.get(pk=request.user.pk)
			entidades = Entidad.objects.filter(sim=sim)
		elif request.user.perfil.tipo == "Laboratorio":
			region = None
			laboratorio = User.objects.get(pk=request.user.pk)
			entidades = Entidad.objects.filter(laboratorio=laboratorio)
		elif request.user.perfil.tipo == "PQ" or request.user.perfil.tipo == "Administrador" or request.user.perfil.tipo == "PM" or request.user.perfil.tipo == "INIFED"  or  request.user.perfil.tipo == "Invitado":
			region = Region.objects.get(numero=numero)
			entidades = Entidad.objects.filter(region=region)			

		context = {
			'region': region,
			'entidades': entidades,
		}
		return render(request,template_name, context)

#Lista de zonas
class ListViewZonas(View):
	@method_decorator(login_required)
	def get(self, request, slug):
		template_name = "accounts/listZonas.html"
		entidad = Entidad.objects.get(slug=slug)
		entidad.CountEscuelas()
		zonas = Zona.objects.filter(entidad=entidad)
		municipios = Municipio.objects.filter(zona__in=zonas)
		region = Region.objects.get(entidad=entidad)
		
		EdicionEntidadForm = EntidadUpdateForm(instance=entidad)

		ListMunicipiosPorZona = []
		for zona in zonas:
			ListMunicipiosPorZona.append({'zona': zona, 'municipios': Municipio.objects.filter(zona=zona)})
		
		context = {
			'entidad': entidad,
			'ListMunicipiosPorZona': ListMunicipiosPorZona,
			'region': region,
			'EdicionEntidadForm': EdicionEntidadForm,
		}
		return render(request,template_name, context)
	def post(self, request, slug):
		entidad = Entidad.objects.get(slug=slug)
		EdicionEntidadForm = EntidadUpdateForm(instance=entidad, files=request.FILES)

		if EdicionEntidadForm.is_valid():
			EdicionEntidadForm.save()
			messages.success(request, "Actualización exitosa")

		return redirect("accounts:ListViewZonas", slug=entidad.slug)

#Lista de escuelas
class ListViewEscuelas(View):
	@method_decorator(login_required)
	def get(self, request, pk=None):
		template_name = "accounts/listEscuelas.html"

		municipio = Municipio.objects.get(pk=pk)
		perfiles = Perfil.objects.filter(municipio=municipio)
		escuelas = User.objects.filter(perfil__in=perfiles).order_by('perfil__localidad', 'perfil__nivel_educativo')
		zona = Zona.objects.get(municipio=municipio)
		entidad = Entidad.objects.get(zona=zona)
		municipio.CountEscuelas()

		context = {
			'municipio': municipio,
			'escuelas': escuelas,
			'entidad': entidad,
		}
		return render(request,template_name, context)

#Detalle de escuela
class DetailViewEscuela(View):
	@method_decorator(login_required)	
	def get(self, request, username):
		template_name = "accounts/detailEscuela.html"
		escuela = User.objects.get(username=username)
		perfil = Perfil.objects.get(user=escuela)
		municipio = Municipio.objects.get(perfil=perfil)
		zona = Zona.objects.get(municipio=municipio)
		entidad = Entidad.objects.get(zona=zona)
		region = Region.objects.get(entidad=entidad)

		try: 
			perfilesRTs = Perfil.objects.filter(residente_tecnico_inifed=entidad)
			rts = User.objects.filter(perfil__in=perfilesRTs)

			perfilesROs = Perfil.objects.filter(residente_obra_ejecutora=entidad)
			ros = User.objects.filter(perfil__in=perfilesROs)

		except Perfil.DoesNotExist:
			perfilesRTs = None
			rts = None
			perfilesROs = None
			ros = None

		try:
			visitaDeAcuerdo = VisitaDeAcuerdo.objects.get(escuela=escuela)
		except VisitaDeAcuerdo.DoesNotExist:
			visitaDeAcuerdo = None

		try:
			primerPrueba = PrimerPrueba.objects.get(escuela=escuela)				
		except PrimerPrueba.DoesNotExist:
			primerPrueba = None

		try:
			sistemaBebedero = SistemaBebedero.objects.get(escuela=escuela)
		except SistemaBebedero.DoesNotExist:
			sistemaBebedero = None

		try:
			inicioDeTrabajo = InicioDeTrabajo.objects.get(escuela=escuela)
		except InicioDeTrabajo.DoesNotExist:
			inicioDeTrabajo = None

		try:
			evidenciasConstruccion = EvidenciaConstruccion.objects.filter(escuela=escuela)
			evidenciaFinal = evidenciasConstruccion.filter(fase="Instalación de Mueble Bebedero", aprobacion_SI = "Aprobado")
		except EvidenciaConstruccion.DoesNotExist:
			evidenciasConstruccion = None
			evidenciaFinal = None

		try:
			segundaPrueba = SegundaPrueba.objects.get(escuela=escuela)
		except SegundaPrueba.DoesNotExist:
			segundaPrueba = None

		try:
			funcionamiento = InicioFuncionamiento.objects.get(escuela=escuela)
		except InicioFuncionamiento.DoesNotExist:
			funcionamiento = None

		try:
			mantenimientos = Mantenimiento.objects.filter(escuela=escuela)
		except Mantenimiento.DoesNotExist:
			mantenimientos = None

		try: 
			actaEntrega = ActaEntrega.objects.get(escuela=escuela)
		except ActaEntrega.DoesNotExist:
			actaEntrega = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'visitaDeAcuerdo': visitaDeAcuerdo,
			'sistemaBebedero': sistemaBebedero,
			'primerPrueba': primerPrueba,
			'inicioDeTrabajo': inicioDeTrabajo,
			'evidenciasConstruccion': evidenciasConstruccion,
			'evidenciaFinal': evidenciaFinal,
			'segundaPrueba': segundaPrueba,
			'funcionamiento': funcionamiento,
			'mantenimientos': mantenimientos,
			'actaEntrega': actaEntrega,
			'municipio': municipio,
			'zona': zona,
			'entidad': entidad,
			'region': region,
			'rts': rts,
			'ros': ros,
		}
		return render(request,template_name, context)

#Creación de escuela
class CreateViewEscuela(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "accounts/createEscuela.html"
		municipio = Municipio.objects.get(pk=pk)
		zona = Zona.objects.get(municipio=municipio)
		entidad = Entidad.objects.get(zona=zona)

		NuevaEscuelaUserForm = EscuelaUserCreateForm()
		NuevaEscuelaPerfilForm = EscuelaPerfilCreateForm()	
		NuevoBebederoForm = BebederoCreateForm()

		context = {
			'municipio': municipio,
			'NuevaEscuelaUserForm': NuevaEscuelaUserForm,
			'NuevaEscuelaPerfilForm': NuevaEscuelaPerfilForm,
			'NuevoBebederoForm': NuevoBebederoForm
		}
		return render(request,template_name, context)
	def post(self, request, pk):
		template_name = "accounts/createEscuela.html"		
		municipio = Municipio.objects.get(pk=pk)
		zona = Zona.objects.get(municipio=municipio)
		entidad = Entidad.objects.get(zona=zona)

		NuevaEscuelaUserForm = EscuelaUserCreateForm(request.POST)
		NuevaEscuelaPerfilForm = EscuelaPerfilCreateForm(request.POST)
		NuevoBebederoForm = BebederoCreateForm(request.POST)

		if NuevaEscuelaUserForm.is_valid() and NuevaEscuelaPerfilForm.is_valid() and NuevoBebederoForm.is_valid():
#		if NuevaEscuelaUserForm.is_valid():
			NuevaEscuelaUser = NuevaEscuelaUserForm.save(commit=False)
			NuevaEscuelaUser.set_password('generica')
			NuevaEscuelaUser.save()

#		if NuevaEscuelaPerfilForm.is_valid():
			NuevaEscuelaPerfil = NuevaEscuelaPerfilForm.save(commit=False)
			NuevaEscuelaPerfil.user = NuevaEscuelaUser
			NuevaEscuelaPerfil.tipo = "Escuela"
			NuevaEscuelaPerfil.municipio = municipio
			NuevaEscuelaPerfil.save()

#		if NuevoBebederoForm.is_valid():
			NuevoBebedero = NuevoBebederoForm.save(commit=False)
			NuevoBebedero.escuela = NuevaEscuelaUser
			NuevoBebedero.save()
			NuevoBebedero.CalculaCTP()
			municipio.CountEscuelas()
			entidad.CountEscuelas()
			
		else:
			context = {
				'municipio': municipio,
				'NuevaEscuelaUserForm': NuevaEscuelaUserForm,
				'NuevaEscuelaPerfilForm': NuevaEscuelaPerfilForm,
				'NuevoBebederoForm': NuevoBebederoForm				
			}
			return render(request,template_name,context)			
		return redirect("accounts:ListViewEscuelas", pk=municipio.pk)

#Actualización de escuela
class UpdateViewEscuela(View):
	@method_decorator(login_required)
	def get(self, request, username):
		template_name = "accounts/updateEscuela.html"
		#perfil = Perfil.objects.get(pk=pk)
		escuela = User.objects.get(username=username)
		perfil = Perfil.objects.get(user=escuela)

		EdicionEscuelaUserForm = EscuelaUserUpdateForm(instance=escuela)
		EdicionEscuelaPerfilForm = EscuelaPerfilUpdateForm(instance=perfil)

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'EdicionEscuelaUserForm': EdicionEscuelaUserForm,
			'EdicionEscuelaPerfilForm': EdicionEscuelaPerfilForm,
		}
		return render(request,template_name, context)
	def post(self, request, username):
		escuela = User.objects.get(username=username)
		perfil = Perfil.objects.get(user=escuela)
		
		EdicionEscuelaUserForm = EscuelaUserUpdateForm(instance=escuela, data=request.POST)
		EdicionEscuelaPerfilForm = EscuelaPerfilUpdateForm(instance=perfil, data=request.POST, files=request.FILES)		

		if EdicionEscuelaUserForm.is_valid():
			EdicionEscuelaUserForm.save()
			messages.success(request, "Actualización exitosa")

		if EdicionEscuelaPerfilForm.is_valid():
			EdicionEscuelaPerfilForm.save()

		return redirect("accounts:UpdateViewEscuela", username=escuela.username)

#Vizualicación de un mapa
class DetailViewMapa(View):
	@method_decorator(login_required)	
	def get(self, request, pk):
		template_name = "accounts/detailMapa.html"
		perfil = Perfil.objects.get(pk=pk)
		escuela = User.objects.get(perfil=perfil)
		
		context = {
			'perfil': perfil,
			'escuela': escuela,
		}
		return render(request,template_name, context)

#Buscador de escuelas
class SearchViewEscuelas(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/searchEscuelas.html"
		query = request.GET.get("query")

		if query:
			perfiles = Perfil.objects.filter(tipo="Escuela")
			escuelas = User.objects.filter(perfil__in=perfiles ,username__contains=query)
		else:
			escuelas = []
	
		context = {
			'escuelas': escuelas,
		}
		return render(request,template_name, context)

#Reporte de avance por escuela
class ListViewAvanceEscuelas(View):
	@method_decorator(login_required)
	def get(self, request, slug):
		template_name = "accounts/listAvanceEscuelas.html"
		
		entidad = Entidad.objects.get(slug=slug)
		zonas = Zona.objects.filter(entidad=entidad)
		municipios = Municipio.objects.filter(zona__in=zonas)
		perfilesEscuelas = Perfil.objects.filter(municipio__in=municipios)
		escuelas = User.objects.filter(perfil__in=perfilesEscuelas).order_by('perfil__municipio__nombre', 'perfil__localidad', 'perfil__nivel_educativo')

		AvancePorEscuelas = []

		for escuela in escuelas:
			try:
				primerPrueba = PrimerPrueba.objects.get(escuela=escuela)
			except PrimerPrueba.DoesNotExist:
				primerPrueba = None

			try:
				inicioDeTrabajo = InicioDeTrabajo.objects.filter(escuela=escuela)
			except InicioDeTrabajo.DoesNotExist:
				inicioDeTrabajo = None

			try:
				visitaDeAcuerdo = VisitaDeAcuerdo.objects.get(escuela=escuela)
			except VisitaDeAcuerdo.DoesNotExist:
				visitaDeAcuerdo = None

			try:
				sistemaBebedero = SistemaBebedero.objects.get(escuela=escuela)
			except SistemaBebedero.DoesNotExist:
				sistemaBebedero = None

			try:
				evidencias = EvidenciaConstruccion.objects.filter(escuela=escuela)
			except EvidenciaConstruccion.DoesNotExist:
				evidencias = None

			try:
				segundaPrueba = SegundaPrueba.objects.get(escuela=escuela)
			except SegundaPrueba.DoesNotExist:
				segundaPrueba = None

			try: 
				inicioFuncionamiento = InicioFuncionamiento.objects.get(escuela=escuela)
			except InicioFuncionamiento.DoesNotExist:
				inicioFuncionamiento = None

			try:
				mantenimientos = Mantenimiento.objects.filter(escuela=escuela)
			except Mantenimiento.DoesNotExist:
				mantenimientos = None

			try: 
				actaEntrega = ActaEntrega.objects.get(escuela=escuela)
			except ActaEntrega.DoesNotExist:
				actaEntrega = None

			data = {'escuela' : escuela, 'primerPrueba': primerPrueba, 'inicioDeTrabajo': inicioDeTrabajo, 'visitaDeAcuerdo': visitaDeAcuerdo, 'sistemaBebedero': sistemaBebedero, 'evidencias': evidencias, 'segundaPrueba': segundaPrueba, 'inicioFuncionamiento': inicioFuncionamiento, 'mantenimientos': mantenimientos, 'actaEntrega': actaEntrega}
			AvancePorEscuelas.append(data)
			paginator = Paginator(AvancePorEscuelas, 12)
			page = request.GET.get('page')
			try:
				escuelas = paginator.page(page)
			except PageNotAnInteger:
				escuelas = paginator.page(1)
			except EmptyPage:
				escuelas = paginator.page(paginator.num_pages)

		context = {
			'AvancePorEscuelas': AvancePorEscuelas,
			'entidad': entidad,
			'escuelas': escuelas,
		}
		return render(request,template_name, context)

#Export ZIP
def ExportExpedienteZIP(request, pk):
	escuela = get_object_or_404(User, pk=pk)
	origen = settings.BASE_DIR
	visitaDeAcuerdo = VisitaDeAcuerdo.objects.get(escuela=escuela)	
	primerPrueba = PrimerPrueba.objects.get(escuela=escuela)
	segundaPrueba = SegundaPrueba.objects.get(escuela=escuela)
	inicioFuncionamiento = InicioFuncionamiento.objects.get(escuela=escuela)

	#Archivos
	cedulaIdentificacion = origen + str(visitaDeAcuerdo.cedula_identificacion.url)
	planoConjunto = origen + str(visitaDeAcuerdo.plano_conjunto.url)
	distribucionPlanta = origen + str(visitaDeAcuerdo.distribucion_planta.url)
	memoriaCalculo = origen + str(visitaDeAcuerdo.memoria_calculo.url)
	planoInstalacionElectrica = origen + str(visitaDeAcuerdo.plano_instalacion_electrica.url)
	planoInstalacionHidraulica = origen + str(visitaDeAcuerdo.plano_instalacion_hidraulica.url)
	planoInstalacionSanitaria = origen + str(visitaDeAcuerdo.plano_instalacion_sanitaria.url)
	foto1PrimerPrueba = origen + str(primerPrueba.foto_toma_agua_1.url)
	foto2PrimerPrueba = origen + str(primerPrueba.foto_toma_agua_2.url)
	foto1SegundaPrueba = origen + str(segundaPrueba.foto_toma_agua_1.url)
	foto2SegundaPrueba = origen + str(segundaPrueba.foto_toma_agua_2.url)
	videoInicioFuncionamiento = origen + str(inicioFuncionamiento.video.url)

	filenames = [cedulaIdentificacion, planoConjunto, distribucionPlanta, memoriaCalculo, planoInstalacionElectrica, planoInstalacionHidraulica, planoInstalacionSanitaria, foto1PrimerPrueba, foto2PrimerPrueba, foto1SegundaPrueba, foto2SegundaPrueba, videoInicioFuncionamiento]

	zip_subdir = "Expediente técnico " + str(escuela.username)
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

def ExportExpedienteZIP(request, pk):
	escuela = get_object_or_404(User, pk=pk)
	origen = settings.BASE_DIR
	visitaDeAcuerdo = VisitaDeAcuerdo.objects.get(escuela=escuela)	
	primerPrueba = PrimerPrueba.objects.get(escuela=escuela)
	segundaPrueba = SegundaPrueba.objects.get(escuela=escuela)
	inicioFuncionamiento = InicioFuncionamiento.objects.get(escuela=escuela)

	#Archivos
	cedulaIdentificacion = origen + str(visitaDeAcuerdo.cedula_identificacion.url)
	planoConjunto = origen + str(visitaDeAcuerdo.plano_conjunto.url)
	distribucionPlanta = origen + str(visitaDeAcuerdo.distribucion_planta.url)
	memoriaCalculo1 = origen + str(visitaDeAcuerdo.memoria_calculo_1.url)
	memoriaCalculo2 = origen + str(visitaDeAcuerdo.memoria_calculo_2.url)
	memoriaCalculo3 = origen + str(visitaDeAcuerdo.memoria_calculo_3.url)
	isometricoInstalacion = origen + str(visitaDeAcuerdo.isometrico_instalacion.url)
	foto1PrimerPrueba = origen + str(primerPrueba.foto_toma_agua_1.url)
	foto2PrimerPrueba = origen + str(primerPrueba.foto_toma_agua_2.url)
	foto1SegundaPrueba = origen + str(segundaPrueba.foto_toma_agua_1.url)
	foto2SegundaPrueba = origen + str(segundaPrueba.foto_toma_agua_2.url)
	videoInicioFuncionamiento = origen + str(inicioFuncionamiento.video.url)

	filenames = [cedulaIdentificacion, planoConjunto, distribucionPlanta, memoriaCalculo1, memoriaCalculo2, memoriaCalculo3, isometricoInstalacion, foto1PrimerPrueba, foto2PrimerPrueba, foto1SegundaPrueba, foto2SegundaPrueba, videoInicioFuncionamiento]

	zip_subdir = "Expediente técnico " + str(escuela.username)
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

def ExportFotosEvidenciaZIP(request, pk):
	escuela = get_object_or_404(User, pk=pk)
	evidencias = EvidenciaConstruccion.objects.filter(escuela=escuela).order_by('creacion')
	origen = settings.BASE_DIR

	filenames = []

	for evidencia in evidencias:
		foto = origen + str(evidencia.foto.url)
		filenames.append(foto)

	zip_subdir = "Reporte fotográfico de " + str(escuela.username)
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

def ExportAvancePorEscuelasCSV(request, pk):
	entidad = get_object_or_404(Entidad, pk=pk)
	zonas = Zona.objects.filter(entidad=entidad)
	municipios=Municipio.objects.filter(zona__in=zonas)
	perfiles = Perfil.objects.filter(municipio__in=municipios)

	ahora = datetime.now().strftime("%d-%m-%Y %H:%M")
	
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="Reporte general de ' + entidad.nombre + ' ' + ahora +'.csv"'
	writer = csv.writer(response)
	writer.writerow(['Municipio', 'Localidad', 'Domicilio', 'C. C. T.','Nombre', 'Nivel educativo', 'Plantilla escolar', 'Mueble', 'Sistema potabilizador', 'Fecha de muestreo', 'Validación de primer prueba', 'Acta de ubicación', 'Cedula de identificación','Convenio de concertación', 'Constancia de integración de comité', 'Plano de conjunto', 'Distribución en planta', 'Memoria de cálculo hidráulico', 'Memoria de cálculo sanitario', 'Memoria de cálculo electrico', 'Isométricos', 'Acta de inicio de trabajo', 'Porcentaje de construcción', 'Salida de mueble', 'Validación de sistema potabilizador', 'Inicio de funcionamiento', 'Mantenimientos', 'Acta de entrega', 'Director', 'Teléfono'])

	escuelas = User.objects.filter(perfil__in=perfiles).values_list('perfil__municipio__nombre', 'perfil__localidad', 'perfil__domicilio', 'username', 'first_name', 'perfil__nivel_educativo', 'perfil__plantilla_escolar', 'escuela__mueble__modelo', 'escuela__sistema_potabilizacion__tipo', 'escuela_primer_prueba__creacion', 'escuela_primer_prueba__validacion', 'escuela_visita_acuerdo__acta_ubicacion', 'escuela_visita_acuerdo__cedula_identificacion', 'escuela_visita_acuerdo__convenio_concertacion', 'escuela_visita_acuerdo__constancia_integracion_comite', 'escuela_visita_acuerdo__plano_conjunto', 'escuela_visita_acuerdo__distribucion_planta', 'escuela_visita_acuerdo__memoria_calculo_1', 'escuela_visita_acuerdo__memoria_calculo_2', 'escuela_visita_acuerdo__memoria_calculo_3', 'escuela_visita_acuerdo__isometrico_instalacion', 'escuela_inicio_trabajo__acta_inicio', 'perfil__avance', 'escuela__packing_list', 'escuela_segunda_prueba__validacion', 'escuela_inicio_funcionamiento__creacion', 'perfil__mantenimientos', 'escuela_acta_entrega__creacion', 'perfil__director', 'perfil__telefono')
	for escuela in escuelas:
		writer.writerow(escuela)

	return response

class ViewHome(View):
	def get(self, request):
		if request.user.is_authenticated == True:
			return redirect('accounts:ViewProfile')
		else:
			template_name = "accounts/home.html"
			return render(request, template_name)		