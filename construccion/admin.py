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

class EvidenciaAdmin(admin.ModelAdmin):
    list_display = ['escuela', 'fase', 'aprobacion_SI']
    search_fields = ['escuela__get_full_name', 'escuela__username']
    list_filter = ['fase', 'aprobacion_SI']
admin.site.register(EvidenciaConstruccion, EvidenciaAdmin)