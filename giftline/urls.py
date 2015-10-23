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
from intercambios import urls as intercambios_urls
from intercambios import views as intercambios_views
from userprofiles import views as user_views

urlpatterns = [
    url(r'^$', intercambios_views.IndexView.as_view(), name='index'),
    url(r'^signup/$', user_views.SignupView.as_view(), name='signup'),
    url(r'^signin/$', user_views.SigninView.as_view(), name='signin'),
    url(r'^signout/$', user_views.SignoutView.as_view(), name='signout'),
    url(r'app/', include(intercambios_urls, namespace='app')),
    url(r'^admin/', include(admin.site.urls)),
]
