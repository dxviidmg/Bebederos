from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^construccion/inicio_de_trabajo/(?P<pk>\d+)/$', views.ViewInicioDeTrabajo.as_view(), name="ViewInicioDeTrabajo"),
#	url(r'^visita/al_sitio/(?P<pk>\d+)/$', views.ViewVisitaAlSitio.as_view(), name="ViewVisitaAlSitio"),
]