from django.conf.urls import url
from secret import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]