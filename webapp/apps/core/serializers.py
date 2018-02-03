from rest_framework import serializers

from . import models


class ContactUsSerializer(serializers.ModelSerializer):
    """Contact us serializer"""

    class Meta:
        model = models.ContactUs
        exclude = ('id',)
