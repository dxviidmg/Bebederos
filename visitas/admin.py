from django.contrib import admin
from .models import *

class PrimerVisitaAdmin(admin.ModelAdmin):
    list_display = ['escuela']
    search_fields = ['escuela__get_full_name', 'escuela__username']

admin.site.register(PrimerVisita, PrimerVisitaAdmin)

class SegundaVisitaAdmin(admin.ModelAdmin):
    list_display = ['escuela']
    search_fields = ['escuela__get_full_name', 'escuela__username']

admin.site.register(SegundaVisita, SegundaVisitaAdmin)