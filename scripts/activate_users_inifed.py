from accounts.models import Perfil
from django.contrib.auth.models import User

def run():
	perfiles = Perfil.objects.filter(tipo='INIFED')
#	print(perfiles)
	users_inifed = User.objects.filter(perfil__in=perfiles).update(is_active=True)
	print("Activación de usuarios de INIFED completada!")

	users_activos = User.objects.filter(is_active=True)