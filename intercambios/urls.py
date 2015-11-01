from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^intercambios/$', views.IntercambiosListView.as_view(), name='intercambios'),
    url(r'^intercambio/(?P<pk>[0-9]+)/$', views.IntercambioDetailView.as_view(), name='intercambio'),
    url(r'^crear', views.CrearIntercambioView.as_view(), name='crear'),
    url(r'^invitar/(?P<pk>[0-9]+)/$', views.invitar, name='invitar'),
]