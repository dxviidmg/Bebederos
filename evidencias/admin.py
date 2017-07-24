from django.contrib import admin
from .models import *

class EvidenciaPreviaAdmin(admin.ModelAdmin):
	model = EvidenciaPrevia
	list_display = ['pk', 'nombre', 'sistemabebedero', 'aprobado', 'creacion', 'subido_por']
	search_fields = ('pk', 'nombre', 'aprobado', 'creacion', 'subido_por__username','subido_por__first_name', 'subido_por__last_name', 'sistemabebedero__escuela__username', 'sistemabebedero__escuela__first_name', 'sistemabebedero__escuela__last_name', )

admin.site.register(EvidenciaPrevia, EvidenciaPreviaAdmin)

class EvidenciaInstalacionAdmin(admin.ModelAdmin):
	model = EvidenciaPrevia
	list_display = ['pk', 'nombre', 'sistemabebedero', 'aprobado', 'creacion', 'subido_por']
	search_fields = ('pk', 'nombre', 'aprobado', 'creacion', 'subido_por__username','subido_por__first_name', 'subido_por__last_name', 'sistemabebedero__escuela__username', 'sistemabebedero__escuela__first_name', 'sistemabebedero__escuela__last_name', )

admin.site.register(EvidenciaInstalacion, EvidenciaInstalacionAdmin)


class EvidenciaPostInstalacionAdmin(admin.ModelAdmin):
	model = EvidenciaPrevia
	list_display = ['pk', 'nombre', 'sistemabebedero', 'aprobado', 'creacion', 'subido_por']
	search_fields = ('pk', 'nombre', 'aprobado', 'creacion', 'subido_por__username','subido_por__first_name', 'subido_por__last_name', 'sistemabebedero__escuela__username', 'sistemabebedero__escuela__first_name', 'sistemabebedero__escuela__last_name', )

admin.site.register(EvidenciaPostInstalacion, EvidenciaPostInstalacionAdmin)


class PlantillaAdmin(admin.ModelAdmin):
	list_display = ('nombre','file_link')

	def file_link(self, obj):
		if obj.archivo:
			return "<a href='%s' download>Download</a>" % (obj.archivo.url,)
		else:
			return "No attachment"
	file_link.allow_tags = True
	file_link.short_description = 'File Download'

admin.site.register(Plantilla , PlantillaAdmin)