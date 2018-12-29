from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Mantenimiento (models.Model):
	mes_CHOICES = (
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
	tipo_choices =  (
		('Preventivo' , 'Preventivo'),
		('Correctivo' , 'Correctivo'),
	)

	año_choices =  (
		(2017 , '2017'),
		(2018 , '2018'),
		(2019 , '2019'),
		(2020 , '2020'),
		(2021 , '2020'),				
	)

	carnet = models.FileField(verbose_name="Carnet actualizado", upload_to='mantenimientos/%Y/%m/%d/')
	foto_1 = models.FileField(verbose_name="Foto al iniciar el mantenimiento", upload_to='mantenimientos/%Y/%m/%d/', null=True, blank=True)
	foto_2 = models.FileField(verbose_name="Foto al finalizar el mantenimiento", upload_to='mantenimientos/%Y/%m/%d/', null=True, blank=True)
	foto_3 = models.FileField(verbose_name="Foto del medidor", upload_to='mantenimientos/%Y/%m/%d/', null=True, blank=True)
	escuela = models.ForeignKey(User, related_name="escuela_mtto")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	mes = models.CharField(choices=mes_CHOICES, max_length=10)
	año = models.IntegerField(choices=año_choices)
	volumen = models.IntegerField(verbose_name="Volumen indicado en medidor (Litros)")
	tipo = models.CharField(max_length=20, default="Preventivo", choices=tipo_choices)
	descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción")
	fecha = models.DateField(default=timezone.now, verbose_name="Fecha de mantenimiento")

	def __str__(self):
		return '{} {} {}'.format(self.escuela, self.mes, self.año)