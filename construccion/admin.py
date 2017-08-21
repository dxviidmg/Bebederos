from django.contrib import admin
from .models import *

class InicioDeTrabajoAdmin(admin.ModelAdmin):
    list_display = ['escuela']
    search_fields = ['escuela__get_full_name', 'escuela__username']

admin.site.register(InicioDeTrabajo, InicioDeTrabajoAdmin)

class InstalacionBebederoAdmin(admin.ModelAdmin):
    list_display = ['escuela']
    search_fields = ['escuela__get_full_name', 'escuela__username']

admin.site.register(InstalacionBebedero, InstalacionBebederoAdmin)

class TerminoDeTrabajoAdmin(admin.ModelAdmin):
    list_display = ['escuela']
    search_fields = ['escuela__get_full_name', 'escuela__username']

admin.site.register(TerminoDeTrabajo, TerminoDeTrabajoAdmin)

class BitacoraAdmin(admin.ModelAdmin):
    list_display = ['escuela']
    search_fields = ['escuela__get_full_name', 'escuela__username']

admin.site.register(EvidenciaConstruccion, BitacoraAdmin)