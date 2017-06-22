from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from bebederos.models import SistemaBebedero
from evidencias.models import *
from evidencias.forms import *

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

class ListViewEntidades(View):
#	@method_decorator(login_required)
	def get(self, request, numero):
		template_name = "accounts/ListViewEntidades.html"
		region = Region.objects.get(numero=numero)
		entidades = Entidad.objects.filter(region=region)
		context = {
			'region': region,
			'entidades': entidades,
		}
		return render(request,template_name, context)

class ListViewMunicipios(View):
#	@method_decorator(login_required)
	def get(self, request,numero, slug):
		template_name = "accounts/ListViewMunicipios.html"
		entidad = Entidad.objects.get(slug=slug)
		municipios = Municipio.objects.filter(entidad=entidad)
		context = {
			'entidad': entidad,
			'municipios': municipios
		}
		return render(request,template_name, context)

class ListViewEscuelas(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "accounts/ListViewEscuelas.html"
		municipio = Municipio.objects.get(pk=pk)
		perfiles = Perfil.objects.filter(municipio=municipio)

		context = {
			'municipio': municipio,
			'perfiles': perfiles,
		}
		return render(request,template_name, context)

class DetailViewEscuela(View):
	def get(self, request, pk):
		template_name = "accounts/DetailViewEscuela.html"
		user = User.objects.get(pk=request.user.pk)
		perfil = Perfil.objects.get(pk=pk)
		escuela = User.objects.get(perfil=perfil)
		sistemabebedero = SistemaBebedero.objects.get(escuela=escuela)
		evidencias = Evidencia.objects.filter(sistemabebedero=sistemabebedero)
		NuevaEvidenciaForm = EvidenciaCreateForm()
		context = {
			'perfil': perfil,
			'escuela': escuela,
			'sistemabebedero': sistemabebedero,
			'evidencias': evidencias,
			'NuevaEvidenciaForm': NuevaEvidenciaForm
		}
		return render(request,template_name, context)
	def post(self,request, pk):

		template_name = "accounts/DetailViewEscuela.html"
		user = User.objects.get(pk=request.user.pk)
		perfil = Perfil.objects.get(pk=pk)
		escuela = User.objects.get(perfil=perfil)
		sistemabebedero = SistemaBebedero.objects.get(escuela=escuela)
		evidencia = Evidencia.objects.filter(sistemabebedero=sistemabebedero)
		NuevaEvidenciaForm = EvidenciaCreateForm(data=request.POST, files=request.FILES)
		
		if NuevaEvidenciaForm.is_valid(): 
			NuevaEvidencia = NuevaEvidenciaForm.save(commit=False)
			NuevaEvidencia.sistemabebedero = sistemabebedero
			NuevaEvidencia.subido_por = user
			NuevaEvidencia.save()

		return redirect("accounts:DetailViewEscuela", pk=perfil.pk)