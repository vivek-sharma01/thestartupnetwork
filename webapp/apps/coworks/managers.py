from django.db import models
from django.db.models import Q


class CoworkManager(models.Manager):
    """Cowork Manager"""

    def get_coworks_list(self, **kwargs):
        """get coworks list"""
        return self.filter(**kwargs).order_by('-created_at')

    def get_coworks_list_search(self, search_keyword, **kwargs):
        """get coworks list"""
        return self.filter(Q(name__icontains=search_keyword) | Q(location__name__icontains=search_keyword))

    def get_cowork_by_slug(self, slug):
        """get cowork by slug"""
        return self.get(slug=slug)

    def get_similar_coworks(self, locality, cowork):
        """get similar coworks"""
        return self.filter(locality=locality).exclude(id=cowork.id)

    def get_cowork_by_city(self, city, cowork):
        """"""
        return self.filter(location__slug=city, parent_cowork=cowork.parent_cowork).exclude(id=cowork.id)