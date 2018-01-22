from django.db import models
from django.contrib.auth.models import User
from accounts.models import Perfil

class Plantilla(models.Model):
	tipo_choices = (
		("Administrador", "Administrador"),
		("Ejecutora", "Ejecutora"),
		("Escuela", "Escuela"),
		("Laboratorio", "Laboratorio"),
		("INIFED", "INIFED"),
		("PQ", "Procesos Químicos (Calidad de Agua)"),
		("PM", "Planta y Manufactura"),
	)
	
	fase_choices = (
		("1", "Todas"),	
		("2", "Pruebas de calidad de agua"),
		("3", "Visita de acuerdos"),
		("4", "Inicio de trabajo"),	
		("5", "Construcción e instalación de Sistema bebedero"),
		("6", "Inicio de funcionamiento"),
		("7", "Mantenimiento"),
	)

	nombre = models.CharField(max_length=100)
	archivo = models.FileField(upload_to='plantillas/%Y/%m/%d/')
	tipo_usuario = models.CharField(max_length=20, choices=tipo_choices)
	fase = models.CharField(choices=fase_choices, max_length=100)
