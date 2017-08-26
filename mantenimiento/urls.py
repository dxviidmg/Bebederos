from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^mantenimiento/(?P<pk>\d+)/$', views.ViewMantenimientos.as_view(), name="ViewMantenimientos"),
]