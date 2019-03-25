from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^success/$', views.success),
    url(r'^success/goback/$', views.goback),
    url(r'^success/(?P<id>\d+)/destroy/$', views.destroy),
    url(r'^success/create/$', views.create),
    url(r'^success/create/create_wish/$', views.create_wish),
    url(r'^success/(?P<id>\d+)/edit/$', views.edit_wish),
    url(r'^success/(?P<id>\d+)/edit/update/$', views.update),
    url(r'^success/(?P<id>\d+)/granted/$', views.grant),


]