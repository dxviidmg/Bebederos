from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^bebederos/update/(?P<pk>\d+)/$', views.UpdateViewBebedero.as_view(), name="UpdateViewBebedero"),
]