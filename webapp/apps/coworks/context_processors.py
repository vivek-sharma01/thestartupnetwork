from . import models, serializers


def get_locations(request):
    """"""
    cowork_location = models.Location.objects.all()
    location_serializer = serializers.LocationSerializer(cowork_location, many=True)
    return {'cities': location_serializer.data}