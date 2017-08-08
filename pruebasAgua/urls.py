from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^pruebas/primera/(?P<pk>\d+)/$', views.ViewPrimerPrueba.as_view(), name="ViewPrimerPrueba"),
	url(r'^pruebas/segunda/(?P<pk>\d+)/$', views.ViewSegundaPrueba.as_view(), name="ViewSegundaPrueba"),
]