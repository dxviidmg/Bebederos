from django.shortcuts import render, redirect
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

import qrcode

class ViewProfile(View):
#	@method_decorator(login_required)
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

class ListViewRegiones(View):
#	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/listRegiones.html"	
		user = User.objects.get(pk=request.user.pk)
		perfil = Perfil.objects.get(user=user)

		regiones = Region.objects.all()

		context = {
			'regiones': regiones,
		}
		return render(request,template_name, context)

class ListViewPartidas(View):
#	@method_decorator(login_required)
	def get(self, request, numero):
		template_name = "accounts/listPartidas.html"
		region = Region.objects.get(numero=numero)
		partidas = Partida.objects.filter(region=region)
		
		ListEntidadesPorPartida = []

		for partida in partidas:

			ListEntidadesPorPartida.append({'partida': partida.numero, 'entidades': Entidad.objects.filter(partida=partida)})
			
		context = {
			'region': region,
			'ListEntidadesPorPartida': ListEntidadesPorPartida,
		}
		return render(request,template_name, context)

class ListViewZonas(View):
#	@method_decorator(login_required)
	def get(self, request, slug=None):
		template_name = "accounts/listZonas.html"
		ListMunicipiosPorZona = []

		if request.user.perfil.tipo == 'SI':
			zona = request.user.superintendente
			entidad = request.user.superintendente.entidad
			
			region = request.user.superintendente.entidad.partida.region
			ListMunicipiosPorZona.append({'zona': zona.nombre, 'municipios': Municipio.objects.filter(zona=zona)})
		elif slug:
			entidad = Entidad.objects.get(slug=slug)
			zonas = Zona.objects.filter(entidad=entidad)
			municipios = Municipio.objects.filter(zona__in=zonas)
			partida = Partida.objects.get(entidad=entidad)
			region = Region.objects.get(partida=partida)
	
			for zona in zonas:
				ListMunicipiosPorZona.append({'zona': zona.nombre, 'municipios': Municipio.objects.filter(zona=zona)})
		
		context = {
			'entidad': entidad,
			'ListMunicipiosPorZona': ListMunicipiosPorZona,
			'region': region
		}
		return render(request,template_name, context)

class ListViewEscuelas(View):
#	@method_decorator(login_required)
	def get(self, request, pk=None):
		template_name = "accounts/listEscuelas.html"

		if request.user.perfil.tipo == "Ejecutora":
			ejecutora = User.objects.get(pk=request.user.pk)
	
			municipio = None
			sistemaBebederos = SistemaBebedero.objects.filter(ejecutora=ejecutora)

			escuelas = User.objects.filter(escuela__in=sistemaBebederos)
			perfiles = Perfil.objects.filter(user__in=escuelas).order_by('status')
			entidad = None
		else:
			municipio = Municipio.objects.get(pk=pk)
			perfiles = Perfil.objects.filter(municipio=municipio).order_by('status')
			zona = Zona.objects.get(municipio=municipio)
			entidad = Entidad.objects.get(zona=zona)

		context = {
			'municipio': municipio,
			'perfiles': perfiles,
			'entidad': entidad,
		}
		return render(request,template_name, context)

class DetailViewEscuela(View):
	def get(self, request, pk):
		template_name = "accounts/detailEscuela.html"
		user = User.objects.get(pk=request.user.pk)
		perfil = Perfil.objects.get(pk=pk)
		escuela = User.objects.get(perfil=perfil)
		municipio = Municipio.objects.get(perfil=perfil)
		zona = Zona.objects.get(municipio=municipio)
		entidad = Entidad.objects.get(zona=zona)
		partida = Partida.objects.get(entidad=entidad)
		region = Region.objects.get(partida=partida)

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
			'municipio': municipio,
			'zona': zona,
			'entidad': entidad,
			'region': region,
		}
		return render(request,template_name, context)

class CreateViewEscuela(View):
	def get(self, request, pk):
		template_name = "accounts/createEscuela.html"
		municipio = Municipio.objects.get(pk=pk)
		zona = Zona.objects.get(municipio=municipio)
		entidad = Entidad.objects.get(zona=zona)

		NuevaEscuelaUserForm = EscuelaUserCreateForm()
		NuevaEscuelaPerfilForm = EscuelaPerfilCreateForm()	
		NuevoBebederoForm = BebederoCreateForm()

		#Img rq code
		qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_L,
			box_size=10,
			border=4,
		)
		qr.add_data('Some data')
		qr.make(fit=True)

		img = qr.make_image(fill_color="black", back_color="white")
		print(qr)
		print(img)

		context = {
			'municipio': municipio,
			'NuevaEscuelaUserForm': NuevaEscuelaUserForm,
			'NuevaEscuelaPerfilForm': NuevaEscuelaPerfilForm,
			'NuevoBebederoForm': NuevoBebederoForm
		}
		return render(request,template_name, context)
	def post(self, request, pk):
		municipio = Municipio.objects.get(pk=pk)
		zona = Zona.objects.get(municipio=municipio)
		entidad = Entidad.objects.get(zona=zona)

		NuevaEscuelaUserForm = EscuelaUserCreateForm(request.POST)
		NuevaEscuelaPerfilForm = EscuelaPerfilCreateForm(request.POST)
		NuevoBebederoForm = BebederoCreateForm(request.POST)

		if NuevaEscuelaUserForm.is_valid():
			NuevaEscuelaUser = NuevaEscuelaUserForm.save(commit=False)
			NuevoEscuelaUser.set_password('generica')
			NuevaEscuelaUser.save()

		if NuevaEscuelaPerfilForm.is_valid():
			NuevaEscuelaPerfil = NuevaEscuelaPerfilForm.save(commit=False)
			NuevaEscuelaPerfil.user = NuevaEscuelaUser
			NuevaEscuelaPerfil.tipo = "Escuela"
			NuevaEscuelaPerfil.municipio = municipio
			NuevaEscuelaPerfil.save()

		if NuevoBebederoForm.is_valid():
			NuevoBebedero = NuevoBebederoForm.save(commit=False)
			NuevoBebedero.escuela = NuevaEscuelaUser
			NuevoBebedero.save()

		return redirect("accounts:ListViewEscuelas", pk=municipio.pk)

class UpdateViewEscuela(View):
	def get(self, request, pk):
		template_name = "accounts/updateEscuela.html"
		perfil = Perfil.objects.get(pk=pk)
		escuela = User.objects.get(perfil=perfil)
		
		EdicionEscuelaUserForm = EscuelaUserUpdateForm(instance=escuela)
		EdicionEscuelaPerfilForm = EscuelaPerfilUpdateForm(instance=perfil)

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'EdicionEscuelaUserForm': EdicionEscuelaUserForm,
			'EdicionEscuelaPerfilForm': EdicionEscuelaPerfilForm,
		}
		return render(request,template_name, context)

	def post(self, request, pk):
		perfil = Perfil.objects.get(pk=pk)
		escuela = User.objects.get(perfil=perfil)
		
		EdicionEscuelaUserForm = EscuelaUserUpdateForm(instance=escuela, data=request.POST)
		EdicionEscuelaPerfilForm = EscuelaPerfilUpdateForm(instance=perfil, data=request.POST, files=request.FILES)		

		if EdicionEscuelaUserForm.is_valid:
			EdicionEscuelaUserForm.save()
			messages.success(request, "Actualización exitosa")

		if EdicionEscuelaPerfilForm.is_valid:
			EdicionEscuelaPerfilForm.save()

		return redirect("accounts:UpdateViewEscuela", pk=perfil.pk)

class DetailViewMapa(View):
	def get(self, request, pk):
		template_name = "accounts/detailMapa.html"
		perfil = Perfil.objects.get(pk=pk)
		escuela = User.objects.get(perfil=perfil)
		
		context = {
			'perfil': perfil,
			'escuela': escuela,
		}
		return render(request,template_name, context)

class SearchViewEscuelas(View):
#	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/searchEscuelas.html"
		query = request.GET.get("query")

		if query:
			escuelas = User.objects.filter(username__contains=query)
			print(escuelas)
	
		else:
			escuelas = []
	
		context = {
			'escuelas': escuelas,
		}
		return render(request,template_name, context)

class ListViewAvanceEscuelas(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "accounts/listAvanceEscuelas.html"
		entidad = Entidad.objects.get(pk=pk)
		zonas = Zona.objects.filter(entidad=entidad)
		municipios = Municipio.objects.filter(zona__in=zonas)
		perfilesEscuelas = Perfil.objects.filter(municipio__in=municipios)
		escuelas = User.objects.filter(perfil__in=perfilesEscuelas)
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
				mantenimientos = Mantenimiento.objects.filter(escuela=escuela)
			except Mantenimiento.DoesNotExist:
				mantenimientos = None

			data = {'escuela' : escuela, 'primerPrueba': primerPrueba, 'inicioDeTrabajo': inicioDeTrabajo, 'visitaDeAcuerdo': visitaDeAcuerdo, 'sistemaBebedero': sistemaBebedero, 'evidencias': evidencias, 'segundaPrueba': segundaPrueba, 'mantenimientos': mantenimientos}
			AvancePorEscuelas.append(data)

		context = {
			'AvancePorEscuelas': AvancePorEscuelas,
			'entidad': entidad,
		}
		return render(request,template_name, context)

#Lista de Entidades para laboratorios
class ListViewEntidades(View):
#	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/listEntidades.html"

		user = User.objects.get(pk=request.user.pk)
		entidades = Entidad.objects.filter(laboratorio=user)
		
		context = {
			'entidades': entidades,
		}
		return render(request,template_name, context)