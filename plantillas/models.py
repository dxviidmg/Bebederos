from django.db import models

class Plantilla(models.Model):
	tipo_choices = (
		("Administrador", "Administrador"), #Yo
		("CEO", "CEO"), #Carlos, Beto
		("SI", "Superintendente"),
		("Ejecutora", "Ejecutora"),
		("Escuela", "Escuela"),
		("Laboratorio", "Laboratorio"),
		("INIFED", "INIFED"), #INIFED Federal
		("Coor_Estatal", "Coordinador Estatal de INIFED"),
		("RTINIFED", "Residente Técnico de INIFED"),
		("IMTA", "IMTA"),
		("ECA", "Encargado de Calidad de Agua"), #Pilar
		("EMB", "Encargado de Mueble Bebedero"), #RaúL, Héctor
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
	archivo = models.FileField()
	tipo_usuario = models.CharField(max_length=20, choices=tipo_choices)
	fase = models.CharField(choices=fase_choices, max_length=100)
