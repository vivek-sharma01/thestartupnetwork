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
    name = serializers.CharField(source='get_name')
    class Meta:
        model = models.MembershipBenefits
        fields = ('name', 'description', 'suitable_for')


class PricingSerializer(serializers.ModelSerializer):
    """Pricing Serializer"""
    membership = MembershipBenefitSerializer(many=True)

    class Meta:
        model = models.Pricing
        fields = ('membership', 'price')


class LocationSerializer(serializers.ModelSerializer):
    """Pricing Serializer"""
    url = serializers.CharField(source='get_url')
    name = serializers.CharField(source='name_capitalize')

    class Meta:
        model = models.Location
        fields = ('name', 'url', 'slug')


class CoworksListSerializer(serializers.ModelSerializer):
    """regions list serializer"""
    # amenities = AmenityListSerializer(source='amenity', many=True)
    # neighbour_amenities = NeighbourAmenityListSerializer(source='neighbour_amenity', many=True)
    # contact_person = ContactPersonSerializer(many=True)
    # membership = serializers.ListField(source='get_pricing')
    starting_price = serializers.CharField(source='get_minimum_price')
    # banner_image = serializers.CharField(source='')

    class Meta:
        model = models.Cowork
        fields = ('name', 'slug', 'description', 'address', 'starting_price', 'banner_image')
