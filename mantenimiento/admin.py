from django.contrib import admin
from .models import *

#Partidas
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ['escuela', 'mes', 'año']
    search_fields = ['escuela__username']
    list_filter = ['mes', 'año']
admin.site.register(Mantenimiento, MantenimientoAdmin)