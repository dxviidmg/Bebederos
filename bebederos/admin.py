from django.contrib import admin
from .models import *

#Bebederos
class BebederoAdmin(admin.ModelAdmin):
	model = Bebedero
	list_display = ['clave', 'nivel_educativo']

admin.site.register(Bebedero, BebederoAdmin)

#Filtros
class FiltroAdmin(admin.ModelAdmin):
	model = Filtro
	list_display = ['modelo', 'normas_cumplidas']

admin.site.register(Filtro, FiltroAdmin)

#Muebles
class MuebleAdmin(admin.ModelAdmin):
	model = Mueble
	list_display = ['modelo']

admin.site.register(Mueble, MuebleAdmin)

#Sistema de Bebederos
class SistemaBebederoAdmin(admin.ModelAdmin):
	model = SistemaBebedero
	list_display = ['escuela', 'constructora', 'filtro', 'mueble']
	search_fields = ['escuela__first_name', 'constructora__first_name', 'escuela__last_name', 'constructora__last_name', 'filtro__modelo', 'mueble__modelo']

admin.site.register(SistemaBebedero, SistemaBebederoAdmin)