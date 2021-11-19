from django.conf.urls import url
from . import views

urlpatterns = [
    url('series/$', views.listSeries),
    url('series/(?P<id>[0-9]+)$', views.serieDetail),
    url('series/$', views.createSerie)
]