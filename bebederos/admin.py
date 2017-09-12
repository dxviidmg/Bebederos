from django.contrib import admin
from .models import *

class MuebleAdmin(admin.ModelAdmin):
	model = Mueble
	list_display = ['clave']

admin.site.register(Mueble, MuebleAdmin)

#Filtros
class SistemaPotabilizacionAdmin(admin.ModelAdmin):
	model = SistemaPotabilizacion
	list_display = ['tipo']

admin.site.register(SistemaPotabilizacion, SistemaPotabilizacionAdmin)

#Sistema de Bebederos
class SistemaBebederoAdmin(admin.ModelAdmin):
	model = SistemaBebedero
	list_display = ['escuela', 'ejecutora', 'sistema_de_potabilizacion', 'mueble']
	search_fields = ['escuela__first_name', 'constructora__first_name', 'escuela__last_name', 'constructora__last_name', 'sistema_de_potabilizacion__modelo']

admin.site.register(SistemaBebedero, SistemaBebederoAdmin)