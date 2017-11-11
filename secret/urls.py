from django.conf.urls import url
from secret import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/(?P<id>[-\w]+)/$', views.api, name='api'),
    url(r'^(?P<id>[-\w]+)/$', views.index, name='index'),
]