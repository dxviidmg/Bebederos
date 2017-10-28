from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^cedulas_identificacion/export/zip/(?P<pk>\d+)/$', views.ExportCedulasIdentificacionZIP, name='ExportCedulasIdentificacionZIP'),
	url(r'^visita/de_acuerdo/(?P<pk>\d+)/$', views.CRViewVisitaDeAcuerdo.as_view(), name="CRViewVisitaDeAcuerdo"),
	url(r'^visita/entrega/(?P<pk>\d+)/$', views.CRViewInicioFuncionamiento.as_view(), name="CRViewInicioFuncionamiento"),
	url(r'^visita/acta_entrega/(?P<pk>\d+)/$', views.CRViewActaEntrega.as_view(), name="CRViewActaEntrega"),	
]