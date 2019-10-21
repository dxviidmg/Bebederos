from django.contrib.auth.models import User
from accounts.models import Perfil
from django.db.models import Q

def run():
	perfiles = Perfil.objects.all()

	perfiles_activos = perfiles.filter(Q(tipo="Administrador") | Q(tipo="Invitado")).order_by('tipo')
#	print("Perfiles activos", perfiles_activos)

	perfiles_no_activos = perfiles.exclude(id__in=perfiles_activos)
#	print("Perfiles NO activos", perfiles_no_activos)	

	users_no_activos = User.objects.filter(perfil__in=perfiles_no_activos).update(is_active=False, is_staff=False, is_superuser=False)
#	print("USERS NO activos", users_no_activos)
	print("Desactivacion de usuarios completada!!!")

	for perfil_activo in perfiles_activos:
		print(perfil_activo, perfil_activo.user.username)

