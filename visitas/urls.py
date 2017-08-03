from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^visita/de_acuerdo/(?P<pk>\d+)/$', views.ViewVisitaDeAcuerdo.as_view(), name="ViewVisitaDeAcuerdo"),
	url(r'^visita/al_sitio/(?P<pk>\d+)/$', views.ViewVisitaAlSitio.as_view(), name="ViewVisitaAlSitio"),
]