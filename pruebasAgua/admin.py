from django.contrib import admin
from .models import *

class PrimerPruebaAdmin(admin.ModelAdmin):
    list_display = ['escuela']
    search_fields = ['escuela__get_full_name', 'escuela__username']

admin.site.register(PrimerPrueba, PrimerPruebaAdmin)

class SegundaPruebaAdmin(admin.ModelAdmin):
    list_display = ['escuela']
    search_fields = ['escuela__get_full_name', 'escuela__username']

admin.site.register(SegundaPrueba, SegundaPruebaAdmin)