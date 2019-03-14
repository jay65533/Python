from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process/$',views.generate),
    url(r'^goback/$',views.goback)
   # This line has changed! Notice that urlpatterns is a list, the comma is incopy
]                            # anticipation of all the routes that will be coming soo
