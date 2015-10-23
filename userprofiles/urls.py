from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^signin/$', views.SigninView.as_view(), name='signin'),
    url(r'^signout/$', views.SignoutView.as_view(), name='signout'),
]
