from django.conf.urls import url
from . import views


urlpatterns = [
	#DescargasZip
	url(r'^cedulas_identificacion/export/zip/(?P<pk>\d+)/$', views.ExportCedulasIdentificacionZIP, name='ExportCedulasIdentificacionZIP'),
	url(r'^planos_conjunto/export/zip/(?P<pk>\d+)/$', views.ExportPlanosConjuntoZIP, name='ExportPlanosConjuntoZIP'),
	url(r'^distribucion_planta/export/zip/(?P<pk>\d+)/$', views.ExportDistribucionesPlantaZIP, name='ExportDistribucionesPlantaZIP'),
	url(r'^memoria_calculo/export/zip/(?P<pk>\d+)/$', views.ExportMemoriasCalculoZIP, name='ExportMemoriasCalculoZIP'),
	url(r'^plano_instalacion_electrica/export/zip/(?P<pk>\d+)/$', views.ExportPlanosInstalacionElectricaZIP, name='ExportPlanosInstalacionElectricaZIP'),
	url(r'^plano_instalacion_hidraulica/export/zip/(?P<pk>\d+)/$', views.ExportPlanosInstalacionHidraculicaZIP, name='ExportPlanosInstalacionHidraculicaZIP'),
	url(r'^plano_instalacion_sanitaria/export/zip/(?P<pk>\d+)/$', views.ExportPlanosInstalacionSanitariaZIP, name='ExportPlanosInstalacionSanitariaZIP'),
	url(r'^inicio_funcionamiento/export/zip/(?P<pk>\d+)/$', views.ExportActasFuncionamietoZIP, name='ExportActasFuncionamietoZIP'),

	url(r'^visita/de_acuerdo/(?P<pk>\d+)/$', views.CRViewVisitaDeAcuerdo.as_view(), name="CRViewVisitaDeAcuerdo"),
	url(r'^visita/entrega/(?P<pk>\d+)/$', views.CRViewInicioFuncionamiento.as_view(), name="CRViewInicioFuncionamiento"),
	url(r'^visita/acta_entrega/(?P<pk>\d+)/$', views.CRViewActaEntrega.as_view(), name="CRViewActaEntrega"),	
]