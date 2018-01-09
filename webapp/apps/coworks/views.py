from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models, serializers


class CityCoworks(APIView):
    """Coworks in a city"""

    def get(self, request, city):
        """"""
        coworks = models.Cowork.objects.get_coworks_list(**{'location__slug': city}).prefetch_related('amenity',
                                                                                                      'neighbour_amenity',
                                                                                                      'contact_person',
                                                                                                      )
        serializer = serializers.CoworksListSerializer(coworks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CoworkIndex(APIView):
    """"""
    template_name = 'cowork.html'

    def get(self, request):
        """"""
        context = {}
        return render(request, template_name=self.template_name, context=context)


