from django.contrib import admin
from .models import *

class VisitaDeAcuerdoAdmin(admin.ModelAdmin):
    list_display = ['escuela']
    search_fields = ['escuela__username']

admin.site.register(VisitaDeAcuerdo, VisitaDeAcuerdoAdmin)

class InicioFuncionamientoAdmin(admin.ModelAdmin):
    list_display = ['escuela']
    search_fields = ['escuela__username']

admin.site.register(InicioFuncionamiento, InicioFuncionamientoAdmin)

class ActaEntregaAdmin(admin.ModelAdmin):
    list_display = ['escuela']
    search_fields = ['escuela__username']

admin.site.register(ActaEntrega, ActaEntregaAdmin)