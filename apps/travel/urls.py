from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.trips, name='trips'),
    url(r'^add', views.add, name='add_trip'),
    url(r'^create', views.create, name='create'),
    url(r'^destination/(?P<id>\d+)$', views.destination, name='destination'),
    url(r'^join/(?P<id>\d+)$', views.join, name='join')

]
