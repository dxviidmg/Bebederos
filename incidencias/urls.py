from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^incidencias/(?P<pk>\d+)/$', views.ViewIncidencias.as_view(), name="ViewIncidencias"),
]