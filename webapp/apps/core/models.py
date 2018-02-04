from django.db import models

from webapp.apps.coworks import models as cowork_model

class Subscribe(models.Model):
    """
    saves email for subscription
    """
    email = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.email


class ContactUs(models.Model):
    """Contact us model"""
    email = models.CharField(max_length=254)
    name = models.CharField(max_length=254, null= True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    cowork = models.ForeignKey(cowork_model.Cowork, related_name="contact_cowork", null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    request_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "phone: " + str(self.phone) + " email: " + str(self.email)

