from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models, serializers, utils


class CityCoworks(APIView):
    """Coworks in a city"""
    template_name = 'cowork-listing.html'

    def get(self, request, city):
        """"""
        coworks = models.Cowork.objects.get_coworks_list(**{'location__slug': city})
        serializer = serializers.CoworksListSerializer(coworks, many=True)
        cowork_chunks = [serializer.data[x:x + 4] for x in range(0, len(serializer.data), 4)]

        context = {
            'data': cowork_chunks,
            'city_slug': city,
            # 'cities': utils.get_locations()
        }

        return render(request, template_name=self.template_name, context=context)


class CoworkIndex(APIView):
    """"""
    template_name = 'cowork.html'

    def get(self, request):
        """"""
        space_types = models.MembershipBenefits.objects.all()
        serializer = serializers.MembershipBenefitSerializer(space_types, many=True)
        most_popular_coworks = models.Cowork.objects.filter(name__icontains='spring').values('name', 'location__name')

        context = {
            'space_types': serializer.data,
            'most_popular_coworks': most_popular_coworks
        }
        return render(request, template_name=self.template_name, context=context)


