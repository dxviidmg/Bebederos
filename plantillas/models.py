from django.db import models
from django.contrib.auth.models import User
from accounts.models import Perfil
class Plantilla(models.Model):
	tipo_choices = (
		("Administrador", "Administrador"), #Yo
		("SI", "Superintendente"),
		("Ejecutora", "Ejecutora"),
		("Escuela", "Escuela"),
		("Laboratorio", "Laboratorio"),
		("INIFED", "INIFED"), #INIFED Federal
		("CEstatal", "Coordinador Estatal de INIFED"),
		("IMTA", "IMTA"),
		("PQ", "Procesos Químicos (Calidad de Agua)"), #Pilar, #Isauri
		("PM", "Planta y Manufactura"), #Raúl, Héctor
	)
	
	fase_choices = (
		("Pruebas de calidad de agua", "Pruebas de calidad de agua"),
		("Inicio de trabajo", "Inicio de trabajo"),	
		("Visita de acuerdos", "Visita de acuerdos"),
		("Construcción e instalación de Sistema bebedero", "Construcción e instalación de Sistema bebedero"),
		("Inicio de funcionamiento", "Inicio de funcionamiento"),
		("Mantenimiento", "Mantenimiento"),
	)
	nombre = models.CharField(max_length=100)
	archivo = models.FileField(upload_to='plantillas/%Y/%m/%d/')
	tipo_usuario = models.CharField(max_length=20, choices=tipo_choices)
	fase = models.CharField(choices=fase_choices, max_length=100)
