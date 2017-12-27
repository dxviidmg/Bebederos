from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^pruebas/export/csv/(?P<pk>\d+)/$', views.ExportPruebasPorEscuelasCSV, name='ExportPruebasPorEscuelasCSV'),
	url(r'^pruebas/etiquetas/export/zip/(?P<pk>\d+)/$', views.ExportEtiquetasZIP, name='ExportEtiquetasZIP'),
#	url(r'^pruebas/primera/calcula_sp/(?P<pk>\d+)/$', CalculateViewSistemaPotabilizador.as_view(), name="CalculateViewSistemaPotabilizador"),
	url(r'^pruebas/primera/(?P<pk>\d+)/$', views.CRUViewPrimerPrueba.as_view(), name="CRUViewPrimerPrueba"),
	url(r'^pruebas/segunda/(?P<pk>\d+)/$', views.CRUViewSegundaPrueba.as_view(), name="CRUViewSegundaPrueba"),
]