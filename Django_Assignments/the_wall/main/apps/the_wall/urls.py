from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^success/$', views.success),
    url(r'^success/goback/$', views.goback),
    url(r'^success/create/$', views.create),
    url(r'^success/create_comment/$', views.create_comment),
    url(r'^success/delete_comment/$', views.delete_comment),
    url(r'^success/delete_message/$', views.delete_message),
    url(r'^success/(?P<id>\d+)/edit/$', views.edit_wish),
    url(r'^success/(?P<id>\d+)/edit/update/$', views.update),

]

