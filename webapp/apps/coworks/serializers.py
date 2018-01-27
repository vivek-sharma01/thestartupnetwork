from rest_framework import serializers

from . import models


class AmenityListSerializer(serializers.ModelSerializer):
    """Amenity list serializer"""
    filter_class = serializers.CharField(source='get_filter_class', required=False)

    class Meta:
        model = models.Amenity
        fields = ('name', 'description', 'filter_class', 'filter')


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
    suitable_for = serializers.ListField(source='get_suitable_for')

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
    url = serializers.CharField(source='get_url')
    # banner_image = serializers.CharField(source='')

    class Meta:
        model = models.Cowork
        fields = ('name', 'slug', 'description', 'address', 'starting_price', 'banner_image', 'url')


class CoworksDetailSerializer(serializers.ModelSerializer):
    """regions list serializer"""
    amenities = serializers.DictField(source='get_amenities_list', required=False)
    # neighbour_amenities = NeighbourAmenityListSerializer(source='neighbour_amenity', many=True)
    contact_person = ContactPersonSerializer(many=True)
    pricing = serializers.DictField(source='get_pricing')
    starting_price = serializers.CharField(source='get_minimum_price')
    city = serializers.CharField(source='get_location_name')

    class Meta:
        model = models.Cowork
        fields = ('name', 'slug', 'description', 'address', 'starting_price', 'banner_image',
                  'city', 'amenities', 'contact_person', 'pricing', 'locality', 'parent_cowork',
                  'reasons_to_choose')


class SimilarCoworksDetailSerializer(serializers.ModelSerializer):
    """similar coworks serializer"""
    url = serializers.CharField(source='get_url')
    class Meta:
        model = models.Cowork
        fields = ('name', 'address', 'banner_image', 'url')
