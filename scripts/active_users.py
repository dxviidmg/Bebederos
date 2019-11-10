from django.contrib.auth.models import User
from accounts.models import Perfil
from django.db.models import Q

def run():
	print('1: Ver usuarios activos')
	print('2: Ver todos los usuarios')
	opcion = input('Opcion: ')
	if opcion == '1':
		users = User.objects.filter(is_active=True)
	else:
		perfiles = Perfil.objects.exclude(tipo='Escuela')
		users = User.objects.filter(perfil__in=perfiles)
#	print("USERS NO activos", users_no_activos)
	users.order_by('username')
	for user in users:
		try:
			if opcion == '1':
				print('Username:' + user.username + ' Nombre:' + user.first_name + ' ' + user.last_name + ' Tipo:' + user.perfil.tipo)
			else:	
				status = 'Activo'
				if user.is_active == False:
					status = 'Inactivo'
				print('Username:' + user.username + ' Nombre:' + user.first_name + ' ' + user.last_name + ' Tipo:' + user.perfil.tipo + ' Status: ' + status)
		except Exception as e:
#			print(user, user.username, 'No tiene perfil')
#			print(e)
			pass
