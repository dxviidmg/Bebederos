from django.contrib.auth.models import User
from accounts.models import Perfil
from django.db.models import Q

def run():
	users = User.objects.filter(is_active=True)
#	print("USERS NO activos", users_no_activos)
	for user in users:
		try:
			print(user, user.username, user.perfil.tipo)
		except:
			print(user, user.username, 'No tiene perfil')
