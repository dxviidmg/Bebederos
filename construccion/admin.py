from django.contrib import admin
from .models import *

class InicioDeTrabajoAdmin(admin.ModelAdmin):
    list_display = ['escuela']
    search_fields = ['escuela__username']

admin.site.register(InicioDeTrabajo, InicioDeTrabajoAdmin)

class EnvolventeTerminadaAdmin(admin.ModelAdmin):
    list_display = ['escuela']
    search_fields = ['escuela__username']

admin.site.register(EnvolventeTerminada, EnvolventeTerminadaAdmin)

class EvidenciaAdmin(admin.ModelAdmin):
    list_display = ['escuela', 'fase', 'aprobacion_SI']
    search_fields = ['escuela__username']
    list_filter = ['fase', 'aprobacion_SI']
    
admin.site.register(EvidenciaConstruccion, EvidenciaAdmin)