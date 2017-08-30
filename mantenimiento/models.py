from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Mantenimiento (models.Model):
	Mes_CHOICES = (
		('Enero' , 'Enero'),
		('Febrero' , 'Febrero'),
		('Marzo' , 'Marzo'),
		('Abril' , 'Abril'),
		('Mayo' , 'Mayo'),
		('Junio' , 'Junio'),
		('Julio' , 'Julio'),
		('Agosto' , 'Agosto'),
		('Septiembre' , 'Septiembre'),
		('Octubre' , 'Octubre'),
		('Noviembre' , 'Noviembre'),
		('Diciembre' , 'Diciembre'),
	)
	carnet = models.FileField()
	sim = models.ForeignKey(User, related_name="sim")
	escuela = models.ForeignKey(User, related_name="escuela_mtto")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	mes = models.CharField(choices=Mes_CHOICES, max_length=10)
	año = models.IntegerField()

	def __str__(self):
		return '{} {} {}'.format(self.escuela, self.mes, self.año)

	class Meta:
		ordering = ['creacion']
#		verbose_name_plural = 'Terminos de trabajo'