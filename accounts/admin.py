from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from bebederos.models import *

#Regiones
admin.site.register(Region)

#Partidas
class PartidaAdmin(admin.ModelAdmin):
    list_display = ['region', 'numero']
    search_fields = ['numero', 'region__numero']
    list_filter = ['region']
admin.site.register(Partida, PartidaAdmin)

#Entidades
class EntidadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'partida', 'coordinador_estatal', 'laboratorio']
    search_fields = ['nombre', 'coordinador_estatal__first_name', 'coordinador_estatal__last_name', 'laboratorio__first_name', 'laboratorio__last_name']
    list_filter = ['partida']
    prepopulated_fields = {"slug": ("nombre",)}

admin.site.register(Entidad, EntidadAdmin)

class ZonaAdmin(admin.ModelAdmin):
    list_display = ['entidad', 'nombre']
    search_fields = ['entidad__nombre', 'nombre']
    list_filter = ['entidad']
admin.site.register(Zona, ZonaAdmin)

#Municipios
class MunicipiodAdmin(admin.ModelAdmin):
    list_display = ['zona', 'nombre']
    search_fields = ['zona__nombre','nombre']
    list_filter = ['zona']
    prepopulated_fields = {"slug": ("nombre",)}

admin.site.register(Municipio, MunicipiodAdmin)

#Usuarios (Constructoras, escuelas, SIM, Residentes, etc)
class SistemaBebederosInline(admin.StackedInline):
    model = SistemaBebedero
    can_delete = False
    fk_name = 'escuela'

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (PerfilInline, SistemaBebederosInline)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'user', 'telefono', 'status']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'telefono']
    list_filter = ['tipo', 'nivel_educativo', 'status']

admin.site.register(Perfil, PerfilAdmin)

