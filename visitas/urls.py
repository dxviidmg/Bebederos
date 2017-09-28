from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^visita/de_acuerdo/(?P<pk>\d+)/$', views.ViewVisitaDeAcuerdo.as_view(), name="ViewVisitaDeAcuerdo"),
	url(r'^visita/entrega/(?P<pk>\d+)/$', views.ViewEntregaDeBebedero.as_view(), name="ViewEntregaDeBebedero"),
]