from . import models, serializers


def get_footer_locations(request):
    """"""
    cowork_location = models.Location.objects.all().order_by('name')
    location_serializer = serializers.LocationSerializer(cowork_location, many=True)
    data = location_serializer.data
    data = [data[x:x + 5] for x in range(0, len(data), 5)]
    return {'footer_cities': data}

def get_listing_locations(request):
    """"""
    cowork_location = models.Location.objects.all().order_by('name')
    location_serializer = serializers.LocationSerializer(cowork_location, many=True)
    return {'listing_cities': location_serializer.data}


def get_coworks(request):
    """"""
    coworks = models.Cowork.objects.all()
    serializer = serializers.MostPopularCoworksSerializer(coworks, many=True)
    return {'coworks': serializer.data}