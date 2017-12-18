from django.db import models


class Subscribe(models.Model):
    """
    saves email for subscription
    """
    email = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.email
