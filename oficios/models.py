from django.db import models
from accounts.models import Entidad

class Oficio(models.Model):
	entidad = models.ForeignKey(Entidad)
	nombre = models.CharField(max_length=30, verbose_name="Nombre o número")
	archivo = models.FileField(upload_to='doc/%Y/%m/%d/',)
	fecha = models.DateField(verbose_name="Fecha de subida")