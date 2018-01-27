from django.conf import settings
from django import template
from webapp.apps.coworks import constants

register = template.Library()


@register.simple_tag
def custom_static(path):
    """
    helps to map js files to static js domain
    """
    return settings.STATIC_URL + path


@register.filter
def amenity_filter_class(filter):
    """
    helps to map js files to static js domain
    """
    return constants.AMENITY_FILTER_CSS.get(filter)
