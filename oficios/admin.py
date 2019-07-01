from django.contrib import admin
from .models import *
class OficioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'entidad', 'fecha']

admin.site.register(Oficio, OficioAdmin)