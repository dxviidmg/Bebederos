from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
#from bebederos.models import *

#Regiones
admin.site.register(Region)

#Entidades/partidas
class EntidadAdmin(admin.ModelAdmin):
    list_display = ['region', 'partida', 'nombre']
    search_fields = ['nombre']
    prepopulated_fields = {"slug": ("nombre",)}

admin.site.register(Entidad, EntidadAdmin)

#Municipios
class MunicipiodAdmin(admin.ModelAdmin):
    list_display = ['entidad', 'nombre']
    search_fields = ['entidad__nombre','nombre']
    prepopulated_fields = {"slug": ("nombre",)}

admin.site.register(Municipio, MunicipiodAdmin)

#Usuarios (Constructoras, escuelas, SIM, Residentes, etc)
#class SistemaBebederosInline(admin.StackedInline):
#    model = SistemaBebedero
#    can_delete = False
#    verbose_name_plural = 'Bebederos'
#    fk_name = 'escuela'

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Perfiles'
    fk_name = 'user'

#class CustomUserAdmin(UserAdmin):
#    inlines = (PerfilInline, SistemaBebederosInline)

#    def get_inline_instances(self, request, obj=None):
#        if not obj:
#            return list()
#        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
#admin.site.register(User, CustomUserAdmin)

#class PerfildAdmin(admin.ModelAdmin):
#    list_display = ['tipo', 'user', 'telefono']
#    search_fields = ['tipo','user__username', 'user__first_name', 'user__last_name', 'telefono']

#admin.site.register(Perfil, PerfildAdmin)