from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^construccion/inicio_de_trabajo/(?P<pk>\d+)/$', views.CRViewInicioDeTrabajo.as_view(), name="CRViewInicioDeTrabajo"),
	url(r'^construccion/termino_de_trabajo/(?P<pk>\d+)/$', views.CRViewTerminoDeTrabajo.as_view(), name="CRViewTerminoDeTrabajo"),
	url(r'^construccion/evidencia/update/(?P<pk>\d+)/$', views.UpdateViewEvidencia.as_view(), name="UpdateViewEvidencia"),
	url(r'^construccion/evidencias/(?P<pk>\d+)/$', views.CRViewEvidencias.as_view(), name="CRViewEvidencias"),
]