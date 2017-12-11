from django.conf import settings
from django import template


register = template.Library()


@register.simple_tag
def custom_static(path):
    """
    helps to map js files to static js domain
    """
    return settings.STATIC_URL + path
