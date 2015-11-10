"""giftline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from intercambios import urls as intercambios_urls
from intercambios import views as intercambios_views
from userprofiles import urls as user_urls
from userprofiles import views as user_views

router = routers.DefaultRouter()
router.register(r'intercambios', intercambios_views.IntercambioViewSet)
router.register(r'usuarios', user_views.UserViewSet)


urlpatterns = [
    url(r'^$', intercambios_views.IndexView.as_view(), name='index'),
    url(r'app/', include(intercambios_urls, namespace='app')),
    url(r'^account/', include(user_urls, namespace='account')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += staticfiles_urlpatterns()
