from django.contrib import admin
from .models import *

class PlantillaAdmin(admin.ModelAdmin):
    list_display = ['fase', 'nombre', 'tipo_usuario']
    search_fields = ['nombre',]
    list_filter = ['fase', 'tipo_usuario']
admin.site.register(Plantilla, PlantillaAdmin)