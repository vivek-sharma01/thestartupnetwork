from . import models, serializers


def get_locations():
    """"""
    cowork_location = models.Location.objects.all()
    location_serializer = serializers.LocationSerializer(cowork_location, many=True)
    return location_serializer.data
