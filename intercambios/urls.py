from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^intercambios/$', views.intercambios, name='intercambios'),
    url(r'^intercambio/(?P<id>[0-9]+)/$', views.intercambio, name='intercambio'),
]