from django.db import models


class Subscribe(models.Model):
    """
    saves email for subscription
    """
    email = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.email


class ContactUs(models.Model):
    """Contact us model"""
    email = models.CharField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null= True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return "phone: " + str(self.phone) + " email: " + str(self.email)

