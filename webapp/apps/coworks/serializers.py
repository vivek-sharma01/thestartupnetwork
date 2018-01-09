from rest_framework import serializers

from . import models


class AmenityListSerializer(serializers.ModelSerializer):
    """Amenity list serializer"""

    class Meta:
        model = models.Amenity
        fields = ('name', 'description')


class NeighbourAmenityListSerializer(serializers.ModelSerializer):
    """Amenity list serializer"""

    class Meta:
        model = models.NeighbourAmenity
        fields = ('name', 'description')


class ContactPersonSerializer(serializers.ModelSerializer):
    """Amenity list serializer"""

    class Meta:
        model = models.ContactPerson
        fields = ('name', 'description', 'phone', 'email')


class MembershipBenefitSerializer(serializers.ModelSerializer):
    """Amenity list serializer"""

    class Meta:
        model = models.MembershipBenefits
        fields = ('name', 'description')


class PricingSerializer(serializers.ModelSerializer):
    """Pricing Serializer"""
    membership = MembershipBenefitSerializer(many=True)

    class Meta:
        model = models.Pricing
        fields = ('membership', 'price')


class CoworksListSerializer(serializers.ModelSerializer):
    """regions list serializer"""
    amenities = AmenityListSerializer(source='amenity', many=True)
    neighbour_amenities = NeighbourAmenityListSerializer(source='neighbour_amenity', many=True)
    contact_person = ContactPersonSerializer(many=True)
    membership = serializers.ListField(source='get_pricing')

    class Meta:
        model = models.Cowork
        fields = ('name', 'slug', 'description', 'address', 'amenities', 'neighbour_amenities',
                  'contact_person', 'membership')