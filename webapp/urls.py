"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from webapp.apps.core import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('webapp.apps.coworks.urls')),
    url(r'^coming-soon/', include('webapp.apps.core.urls')),
    url(r'^contact-us-form/$', views.ContactUsForm.as_view(), name='contact-us-form'),
    url(r'^contact-us$', views.ContactUs.as_view(), name='contact-us'),
    url(r'^subscribe/$', views.Subscribe.as_view(), name='subscribe'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
