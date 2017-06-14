from django.contrib import admin
from .models import *

class MuebleAdmin(admin.ModelAdmin):
	model = Mueble
	list_display = ['clave', 'nivel_educativo']

admin.site.register(Mueble, MuebleAdmin)

#Filtros
class FiltroAdmin(admin.ModelAdmin):
	model = Filtro
	list_display = ['modelo', 'normas_cumplidas']

admin.site.register(Filtro, FiltroAdmin)

#Sistema de Bebederos
class SistemaBebederoAdmin(admin.ModelAdmin):
	model = SistemaBebedero
	list_display = ['escuela', 'constructora', 'filtro', 'mueble']
	search_fields = ['escuela__first_name', 'constructora__first_name', 'escuela__last_name', 'constructora__last_name', 'filtro__modelo']

admin.site.register(SistemaBebedero, SistemaBebederoAdmin)