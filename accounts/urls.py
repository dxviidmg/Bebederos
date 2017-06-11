from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
	url(r'^login', login,name="login"),
	url(r'^logout/$', logout, name="logout"),

	url(r'^accounts/profile/$', views.ViewProfile.as_view(), name="ViewProfile"),
#	url(r'^accounts/nuevo/$', views.CreateViewAccount.as_view(), name="CreateViewAccount"),	
#	url(r'^change-password/$', views.ViewChangePassword.as_view(), name='ViewChangePassword'),

#	url(r'^reset-password/$', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),
#	url(r'^reset-password/done/$', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),
#	url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),
#	url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete'),
	url(r'^region/estado/municipio/escuela/(?P<pk>[-\w]+)/$', views.DetailViewEscuela.as_view(), name="DetailViewEscuela"),
	url(r'^region/estado/municipio/(?P<pk>[-\w]+)/$', views.ListViewEscuelas.as_view(), name="ListViewEscuelas"),
	url(r'^region/(?P<numero>[-\w]+)/estado/(?P<slug>[-\w]+)/$', views.ListViewMunicipios.as_view(), name="ListViewMunicipios"),	
	url(r'^region/(?P<numero>[-\w]+)/$', views.ListViewEntidades.as_view(), name="ListViewEntidades"),   
	url(r'^regiones/$', views.ListViewRegiones.as_view(), name="ListViewRegiones"),
    ]


