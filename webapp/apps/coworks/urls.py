
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.CoworkIndex.as_view(), name='cowork-home-page'),
    url(r'^coworks/(?P<city>.+)$', views.CityCoworks.as_view(), name='coworks-list'),

]
