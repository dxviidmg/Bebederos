from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^plantillas/$', views.ListViewPlantillas.as_view(), name="ListViewPlantillas"),
]