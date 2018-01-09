
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.CoworkIndex.as_view(), name='cowork-home-page'),
    url(r'^(?P<city>[\w]+)$', views.CityCoworks.as_view(), name='coworks-list'),

]
