
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^(?P<city>[\w]+)$', views.CityCoworks.as_view(), name='coworks-list'),

]
