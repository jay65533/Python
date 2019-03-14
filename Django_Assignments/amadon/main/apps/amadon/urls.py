from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.redirector),
        url(r'^amadon/$', views.index),
        url(r'amadon/buy/$', views.create),
        url(r'amadon/checkout/$', views.checkout),
        url(r'^amadon/checkout/goback/$',views.goback)
]