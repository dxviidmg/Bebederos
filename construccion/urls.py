from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^construccion/evidencia/(?P<pk>\d+)/$', views.UpdateViewEvidencia.as_view(), name="UpdateViewEvidencia"),
	url(r'^construccion/inicio_de_trabajo/(?P<pk>\d+)/$', views.ViewInicioDeTrabajo.as_view(), name="ViewInicioDeTrabajo"),
	url(r'^construccion/instalacion_bebedero/(?P<pk>\d+)/$', views.ViewInstalacionBebedero.as_view(), name="ViewInstalacionBebedero"),
	url(r'^construccion/termino_de_trabajo/(?P<pk>\d+)/$', views.ViewTerminoDeTrabajo.as_view(), name="ViewTerminoDeTrabajo"),
	url(r'^construccion/bitacora/(?P<pk>\d+)/$', views.ViewBitacora.as_view(), name="ViewBitacora"),
]