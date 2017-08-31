from django.contrib import admin
from .models import *

class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ['escuela', 'status', 'prioridad', 'fase', 'autor']
    search_fields = ['escuela__first_name', 'escuela__username']
    list_filter = ['status', 'prioridad', 'fase']
admin.site.register(Incidencia, IncidenciaAdmin)