from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create/$' , views.create, name = 'c'),
    url(r'^courses/destroy/(?P<id>\d+)/$', views.destroy),
    url(r'^nodelete/$' , views.nodelete, name = 'nodel'),
    url(r'^delete/$' , views.delete, name = 'del')
]