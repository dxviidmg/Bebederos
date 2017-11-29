from django.contrib import admin
from .models import *

class MuebleAdmin(admin.ModelAdmin):
	model = Mueble
	list_display = ['modelo', 'nivel_educativo', 'total_salidas']

admin.site.register(Mueble, MuebleAdmin)

#Filtros
class SistemaPotabilizacionAdmin(admin.ModelAdmin):
	modelo = SistemaPotabilizacion
	list_display = ['tipo']

admin.site.register(SistemaPotabilizacion, SistemaPotabilizacionAdmin)

#Sistema de Bebederos
class SistemaBebederoAdmin(admin.ModelAdmin):
	model = SistemaBebedero
	list_display = ['escuela', 'no_trazabilidad','sistema_potabilizacion', 'mueble']
	search_fields = ['escuela__username', 'escuela__first_name', 'escuela__last_name', 'no_trazabilidad', 'sistema_potabilizacion__tipo']
	list_filter = [ 'mueble',]
admin.site.register(SistemaBebedero, SistemaBebederoAdmin)