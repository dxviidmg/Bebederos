from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^visita/de_acuerdo/(?P<pk>\d+)/$', views.CRViewVisitaDeAcuerdo.as_view(), name="CRViewVisitaDeAcuerdo"),
	url(r'^visita/entrega/(?P<pk>\d+)/$', views.CRViewInicioFuncionamiento.as_view(), name="CRViewInicioFuncionamiento"),
]