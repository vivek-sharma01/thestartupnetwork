from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreConfig(AppConfig):
    name = 'webapp.apps.core'
    verbose_name = _(u'core')


