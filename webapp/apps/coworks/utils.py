from . import models, serializers, constants


def get_locations():
    """"""
    cowork_location = models.Location.objects.all()
    location_serializer = serializers.LocationSerializer(cowork_location, many=True)
    return location_serializer.data

def extract_membership_name(membership):
    return constants.MEMBERSHIPS_ORDERING[constants.MEMBERSHIPS_DICT[membership.get('name')]]
