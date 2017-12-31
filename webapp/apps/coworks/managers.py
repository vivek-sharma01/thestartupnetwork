from django.db import models


class CoworkManager(models.Manager):
    """Cowork Manager"""

    def get_coworks_list(self, **kwargs):
        """get coworks list"""
        return self.filter(**kwargs)
