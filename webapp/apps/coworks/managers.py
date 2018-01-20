from django.db import models
from django.db.models import Q


class CoworkManager(models.Manager):
    """Cowork Manager"""

    def get_coworks_list(self, **kwargs):
        """get coworks list"""
        return self.filter(**kwargs)

    def get_coworks_list_search(self, search_keyword, **kwargs):
        """get coworks list"""
        return self.filter(Q(name__icontains=search_keyword) | Q(location__name__icontains=search_keyword))
