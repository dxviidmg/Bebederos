from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^bebederos/create/(?P<pk>\d+)/$', views.ViewBebederos.as_view(), name="ViewBebederos"),
]