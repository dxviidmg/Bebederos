from django.contrib import admin
from .models import *

class MuebleAdmin(admin.ModelAdmin):
	model = Mueble
	list_display = ['modelo']

admin.site.register(Mueble, MuebleAdmin)

#Filtros
class SistemaPotabilizacionAdmin(admin.ModelAdmin):
	model = SistemaPotabilizacion
	list_display = ['tipo']

admin.site.register(SistemaPotabilizacion, SistemaPotabilizacionAdmin)

#Sistema de Bebederos
class SistemaBebederoAdmin(admin.ModelAdmin):
	model = SistemaBebedero
	list_display = ['escuela', 'no_trazabilidad','sistema_potabilizacion', 'mueble']
	search_fields = ['escuela__username', 'escuela__first_name', 'no_trazabilidad', 'constructora__first_name', 'escuela__last_name', 'constructora__last_name', 'sistema_potabilizacion__modelo']

admin.site.register(SistemaBebedero, SistemaBebederoAdmin)