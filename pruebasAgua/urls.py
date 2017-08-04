from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^pruebas/primera/(?P<pk>\d+)/$', views.ViewPrimerPrueba.as_view(), name="ViewPrimerPrueba"),
#	url(r'^construccion/instalacion_bebedero/(?P<pk>\d+)/$', views.ViewInstalacionBebedero.as_view(), name="ViewInstalacionBebedero"),
#	url(r'^construccion/termino_de_trabajo/(?P<pk>\d+)/$', views.ViewTerminoDeTrabajo.as_view(), name="ViewTerminoDeTrabajo"),	
]