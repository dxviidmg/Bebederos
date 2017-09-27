from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import *
from accounts.models import Perfil
from .forms import *

#Creación y edición de la visita de acuerdo
class ViewBebederos(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "bebederos/createBebedero.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		NuevoBebederoForm = BebederoCreateForm()

		try:
			sistemaBebedero = SistemaBebedero.objects.get(escuela=escuela)
			EdicionBebederoForm = BebederoEditForm(instance=sistemaBebedero)
		except SistemaBebedero.DoesNotExist:
			sistemaBebedero = None
			EdicionBebederoForm = None

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'sistemaBebedero': sistemaBebedero,
			'EdicionBebederoForm': EdicionBebederoForm,
			'NuevoBebederoForm': NuevoBebederoForm,
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

		return redirect("bebederos:ViewBebederos", pk=perfil.pk)		