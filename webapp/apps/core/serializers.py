from rest_framework import serializers

from . import models


class ContactUsSerializer(serializers.ModelSerializer):
    """Amenity list serializer"""

    class Meta:
        model = models.ContactUs
        exclude = ('id',)
