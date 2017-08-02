from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^visitas/alsitio/nuevo/(?P<pk>\d+)/$', views.CreateViewVisitaAlSitio.as_view(), name="CreateViewVisitaAlSitio"),
]