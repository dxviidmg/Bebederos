from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^mantenimientos/(?P<pk>\d+)/$', views.CRViewMantenimientos.as_view(), name="CRViewMantenimientos"),
	url(r'^mantenimiento/update/(?P<pk>\d+)/$', views.UpdateViewMantenimiento.as_view(), name="UpdateViewMantenimiento"),	
]