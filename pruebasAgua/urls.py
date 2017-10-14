from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^pruebas/por_usuario/export/csv/(?P<pk>\d+)/$', views.ExportPruebasPorEscuelasCSV, name='ExportPruebasPorEscuelasCSV'),
	url(r'^pruebas/primera/(?P<pk>\d+)/$', views.CRUViewPrimerPrueba.as_view(), name="CRUViewPrimerPrueba"),
	url(r'^pruebas/segunda/(?P<pk>\d+)/$', views.CRUViewSegundaPrueba.as_view(), name="CRUViewSegundaPrueba"),
]