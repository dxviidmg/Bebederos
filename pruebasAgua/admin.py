from django.contrib import admin
from .models import *

class PrimerPruebaAdmin(admin.ModelAdmin):
    list_display = ['escuela', 'validacion']
    search_fields = ['escuela__first_name', 'escuela__username']
    list_filter = ['validacion']

admin.site.register(PrimerPrueba, PrimerPruebaAdmin)

class SegundaPruebaAdmin(admin.ModelAdmin):
    list_display = ['escuela', 'aprobacion']
    search_fields = ['escuela__first_name', 'escuela__username']
    list_filter = ['aprobacion']

admin.site.register(SegundaPrueba, SegundaPruebaAdmin)