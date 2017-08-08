from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from visitas.models import *
from construccion.models import *
from pruebasAgua.models import *
#from bebederos.models import SistemaBebedero

class ViewProfile(View):
#	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/profile.html"
		
		user = User.objects.get(pk=request.user.pk)
		try:
			perfil = Perfil.objects.get(user=user)
		except:
			perfil = None
		context = {
		'perfil': perfil,
		}
		return render(request,template_name, context)

class ListViewRegiones(View):
#	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/ListViewRegiones.html"
		
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
		template_name = "accounts/ListViewPartidas.html"
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
	def get(self, request, slug):
		template_name = "accounts/ListViewZonas.html"
		entidad = Entidad.objects.get(slug=slug)
		zonas = Zona.objects.filter(entidad=entidad)
		municipios = Municipio.objects.filter(zona__in=zonas)
#		print(municipios)

		ListMunicipiosPorZona = []
		for zona in zonas:
			print(zona)
			ListMunicipiosPorZona.append({'zona': zona.nombre, 'municipios': Municipio.objects.filter(zona=zona)})

			print(ListMunicipiosPorZona)
#			municipios = Municipio.objects.filter(zona=zonas)
#		print(municipios)
		escuelasRegistradas = Perfil.objects.filter(tipo="Escuela", municipio=municipios)
		escuelasAceptadas = escuelasRegistradas.filter(status='Aceptado')
#		print(escuelasAceptadas)
		context = {
			'entidad': entidad,
#			'municipios': municipios,
			'escuelasRegistradas': escuelasRegistradas,
			'escuelasAceptadas': escuelasAceptadas, 
			'ListMunicipiosPorZona': ListMunicipiosPorZona,
		}
		return render(request,template_name, context)

class ListViewEscuelas(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "accounts/ListViewEscuelas.html"
		municipio = Municipio.objects.get(pk=pk)
		perfiles = Perfil.objects.filter(municipio=municipio).order_by('status')
		escuelasAceptadas = perfiles.filter(status="Aceptado")

		context = {
			'municipio': municipio,
			'perfiles': perfiles,
			'escuelasAceptadas': escuelasAceptadas,
		}
		return render(request,template_name, context)

class DetailViewEscuela(View):
	def get(self, request, pk):
		template_name = "accounts/DetailViewEscuela.html"
		user = User.objects.get(pk=request.user.pk)
		perfil = Perfil.objects.get(pk=pk)
		escuela = User.objects.get(perfil=perfil)

		try:
			visitaAlSitio = VisitaAlSitio.objects.get(escuela=escuela)
		except VisitaAlSitio.DoesNotExist:
			visitaAlSitio = None

		try:
			visitaDeAcuerdo = VisitaDeAcuerdo.objects.get(escuela=escuela)
		except VisitaDeAcuerdo.DoesNotExist:
			visitaDeAcuerdo = None

		try:
			primerPrueba = PrimerPrueba.objects.get(escuela=escuela)
			if primerPrueba.aprobacion == "En espera":
				print("No mames wey")
				
		except PrimerPrueba.DoesNotExist:
			primerPrueba = None

		try:
			inicioDeTrabajo = InicioDeTrabajo.objects.get(escuela=escuela)
		except InicioDeTrabajo.DoesNotExist:
			inicioDeTrabajo = None

		try:
			instalacionBebedero = InstalacionBebedero.objects.get(escuela=escuela)
		except InstalacionBebedero.DoesNotExist:
			instalacionBebedero = None

		try:
			terminoDeTrabajo = TerminoDeTrabajo.objects.get(escuela=escuela)
		except TerminoDeTrabajo.DoesNotExist:
			terminoDeTrabajo = None

		try:
			entregaDeBebedero = EntregaDeBebedero.objects.get(escuela=escuela)
		except EntregaDeBebedero.DoesNotExist:
			entregaDeBebedero = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'visitaAlSitio': visitaAlSitio,
			'visitaDeAcuerdo': visitaDeAcuerdo,
			'inicioDeTrabajo': inicioDeTrabajo,
			'instalacionBebedero': instalacionBebedero,
			'terminoDeTrabajo': terminoDeTrabajo,
			'entregaDeBebedero': entregaDeBebedero,
			'primerPrueba': primerPrueba
		}
		return render(request,template_name, context)