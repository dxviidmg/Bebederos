"""Bebederos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

#urls of the apps
from accounts import urls as accountsUrls
from visitas import urls as visitasUrls
from construccion import urls as construccionUrls
from pruebasAgua import urls as pruebasAguaUrls
from incidencias import urls as incidenciasUrls
from mantenimiento import urls as mantenimientoUrls
#Images
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^', include(accountsUrls, namespace="accounts")),
    url(r'^', include(visitasUrls, namespace="visitas")),
    url(r'^', include(construccionUrls, namespace="construccion")),
    url(r'^', include(pruebasAguaUrls, namespace="pruebas")),
    url(r'^', include(incidenciasUrls, namespace="incidencias")),
    url(r'^', include(mantenimientoUrls, namespace="mantenimiento")),
]

#Images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)