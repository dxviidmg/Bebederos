from django.contrib import admin
from .models import *

class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ['escuela', 'mes', 'año', 'sim']
    search_fields = ['escuela__get_full_name', 'escuela__username']
    list_filter = ['mes', 'año']
admin.site.register(Mantenimiento, MantenimientoAdmin)