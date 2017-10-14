from django.contrib import admin
from .models import *

class PlantillaAdmin(admin.ModelAdmin):
    list_display = ['nombre',]
    search_fields = ['nombre',]
    list_filter = ['nombre']
admin.site.register(Plantilla, PlantillaAdmin)