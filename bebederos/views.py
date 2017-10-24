from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import *
from accounts.models import Perfil
from .forms import *
from accounts.models import *
from django.utils.timezone import datetime
from django.contrib import messages
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from datetime import date
from django.contrib import messages

#Librerias para poder exportar PDFs
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

#Actualización de un Sistema Bebedero
class UpdateViewBebedero(View):
#	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "bebederos/updateBebedero.html"
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		municipio = Municipio.objects.get(perfil=perfil)
		zona = Zona.objects.get(municipio=municipio)
		entidad = Entidad.objects.get(zona=zona)
		countSB = SistemaBebedero.objects.all().count()
 
		sistemaBebedero = SistemaBebedero.objects.get(escuela=escuela)
		EdicionBebederoForm1 = BebederoUpdateForm1(instance=sistemaBebedero)
		EdicionBebederoForm2 = BebederoUpdateForm2(instance=sistemaBebedero)
		EdicionBebederoForm3 = BebederoUpdateForm3(instance=sistemaBebedero)

		context = {
			'perfil': perfil,
			'escuela': escuela,
			'entidad': entidad,
			'sistemaBebedero': sistemaBebedero,
			'EdicionBebederoForm1': EdicionBebederoForm1,
			'EdicionBebederoForm2': EdicionBebederoForm2,
			'EdicionBebederoForm3': EdicionBebederoForm3,			
		}
		return render(request, template_name, context)
	def post(self, request, pk):
		perfil = get_object_or_404(Perfil, pk=pk)
		escuela = User.objects.get(perfil=perfil)
		municipio = Municipio.objects.get(perfil=perfil)
		zona = Zona.objects.get(municipio=municipio)
		entidad = Entidad.objects.get(zona=zona)
		countSB = SistemaBebedero.objects.all().count()
		sistemaBebedero = SistemaBebedero.objects.get(escuela=escuela)

		EdicionBebederoForm1 = BebederoUpdateForm1(instance=sistemaBebedero, data=request.POST, files=request.FILES)
		if EdicionBebederoForm1.is_valid():
			EdicionBebederoForm1.save()

		EdicionBebederoForm2 = BebederoUpdateForm2(instance=sistemaBebedero, data=request.POST, files=request.FILES)
		if EdicionBebederoForm2.is_valid():
			EdicionBebederoForm2.save()

		EdicionBebederoForm3 = BebederoUpdateForm3(instance=sistemaBebedero, data=request.POST, files=request.FILES)
		if EdicionBebederoForm3.is_valid():
			EdicionBebederoForm3.save()

			sistemaBebedero.GenerateId()
		
		messages.success(request, "Actualización exitosa")

		return redirect("bebederos:UpdateViewBebedero", pk=perfil.pk)

#Exportación en PDF de guia de trazabilidad
def ExportComprobanteTrazabilidadPDF(request, pk):
	sistemaBebedero =get_object_or_404(SistemaBebedero, pk=pk)
	today = date.today().strftime('%d-%m-%Y')

	doc = SimpleDocTemplate("/tmp/"+ str(sistemaBebedero.no_trazabilidad) +".pdf")
	styles = getSampleStyleSheet()
	Story = [Spacer(1,0*inch)]
	styleTitle = styles["Title"]
	styleText = styles["Heading3"]
	styleText2 = styles["Heading4"]
	styleText3 = styles["Normal"]

	title = ("Guia de trazabilidad")
	t1 = Paragraph(title, styleTitle)
	Story.append(t1)
	Story.append(Spacer(0,0.3*inch))
	
	today = str(today)
	t2 = Paragraph(today, styleText)
	Story.append(t2)
	Story.append(Spacer(0,0.3*inch))

	text = "En el presente documento se hace la ratificación de los siguientes datos:"
	t3 = Paragraph(text, styleText)
	Story.append(t3)

	cct = "Información de la escuela beneficiada:"
	t4 = Paragraph(cct, styleText2)
	Story.append(t4)

	cct = "C. C. T: " + str(sistemaBebedero.escuela.username)
	t5 = Paragraph(cct, styleText3)
	Story.append(t5)

	escuela = "Escuela: " + str(sistemaBebedero.escuela)
	t6 = Paragraph(escuela, styleText3)
	Story.append(t6)

	municipio = "Municipio: " + str(sistemaBebedero.escuela.perfil.municipio.nombre)
	t7 = Paragraph(municipio, styleText3)
	Story.append(t7)

	entidad = "Entidad: " + str(sistemaBebedero.escuela.perfil.municipio.zona.entidad)
	t8 = Paragraph(entidad, styleText3)
	Story.append(t8)

	cct = "Especificaciones del Sistema Bebedero:"
	t9 = Paragraph(cct, styleText2)
	Story.append(t9)

	muebleBebedero = "Modelo de muble: " + str(sistemaBebedero.mueble)
	t10 = Paragraph(muebleBebedero, styleText3)
	Story.append(t10)

	sistemaPotabilizacion = "Sistema de potabilización: " + str(sistemaBebedero.sistema_potabilizacion)
	t11 = Paragraph(sistemaPotabilizacion, styleText3)
	Story.append(t11)

	tanque = "Capacidad de tanque presurizador: " + str(sistemaBebedero.capacidad_tanque_presurizador) + "galones"
	t12 = Paragraph(tanque, styleText3)
	Story.append(t12)


	trazabilidad = "No. de trazabilidad: " + str(sistemaBebedero.no_trazabilidad)
	t13 = Paragraph(trazabilidad, styleText3)
	Story.append(t13)
	Story.append(Spacer(1,0.5*inch))

	firman = "Firman"
	t14 = Paragraph(firman, styleText3)
	Story.append(t14)

	linea1 = "________________________"
	t15 = Paragraph(linea1, styleText)
	Story.append(t15)

	nombre1 = "Ing. Raul A. Mejía Mejía"
	t16 = Paragraph(nombre1, styleText3)
	Story.append(t16)

	puesto1 = "Gerente de Manufactura"
	t17 = Paragraph(puesto1, styleText3)
	Story.append(t17)

	linea2 = "________________________"
	t18 = Paragraph(linea2, styleText)
	Story.append(t18)

	nombre2 = "Ing. Pilar N. Velázquez Serna"
	t19 = Paragraph(nombre2, styleText3)
	Story.append(t19)

	puesto2 = "Gerente de Procesos Quimicos"
	t20 = Paragraph(puesto2, styleText3)
	Story.append(t20)

	linea3 = "________________________"
	t21 = Paragraph(linea3, styleText)
	Story.append(t21)

	nombre3 = "Ing. Héctor M. Rios Sanchez"
	t22 = Paragraph(nombre3, styleText3)
	Story.append(t22)

	puesto3 = "Gerente de Planta"
	t23 = Paragraph(puesto3, styleText3)
	Story.append(t23)

	doc.build(Story)

	fs = FileSystemStorage("/tmp")
	with fs.open(str(sistemaBebedero.no_trazabilidad)+'.pdf') as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename='+str(sistemaBebedero.no_trazabilidad)+'.pdf'
		return response

	return response