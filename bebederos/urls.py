from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^bebederos/trazabilidad/export/pdf/(?P<pk>\d+)/$', views.ExportComprobanteTrazabilidadPDF, name="ExportComprobanteTrazabilidadPDF"),
	url(r'^bebederos/update/(?P<pk>\d+)/$', views.UpdateViewBebedero.as_view(), name="UpdateViewBebedero"),	
]