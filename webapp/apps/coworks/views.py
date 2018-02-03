from django.shortcuts import render
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models, serializers, utils


class CityCoworks(APIView):
    """Coworks in a city"""
    template_name = 'cowork-listing.html'

    def get(self, request, city):
        """
        Args:
            request:
            city: city name to filter the coworks
        Returns: list of coworks
        """
        kwargs = {
            'location__slug': city
        }
        if city == 'india':
            kwargs = {}
        coworks = models.Cowork.objects.get_coworks_list(**kwargs)
        search_keyword = request.GET.get('search')
        if search_keyword:
            coworks = coworks.filter(Q(name__icontains=search_keyword) | Q(location__name__icontains=search_keyword))
        serializer = serializers.CoworksListSerializer(coworks, many=True)
        cowork_chunks = [serializer.data[x:x + 4] for x in range(0, len(serializer.data), 4)]

        context = {
            'data': cowork_chunks,
            'city_slug': city,
            'title': 'Coworking spaces in {}'.format(city)
        }

        return render(request, template_name=self.template_name, context=context)


class CoworkIndex(APIView):
    """"""
    template_name = 'cowork.html'

    def get(self, request):
        """"""
        space_types = models.MembershipBenefits.objects.all()
        serializer = serializers.MembershipBenefitSerializer(space_types, many=True)
        most_popular_coworks = models.Cowork.objects.filter(name__icontains='awfis')#.values('name', 'location__name')
        most_popular_coworks_serializer = serializers.CoworksListSerializer(most_popular_coworks, many=True)
        space_types = sorted(serializer.data, key=utils.extract_membership_name)
        context = {
            'space_types': space_types,
            'most_popular_coworks': most_popular_coworks_serializer.data
        }
        return render(request, template_name=self.template_name, context=context)


class CoworksSearch(APIView):
    """Coworks in a city"""
    template_name = 'cowork-listing.html'

    def get(self, request):
        """
        Args:
            request:
            city: cowork name to filter the coworks
        Returns: list of coworks
        """
        search_keyword = request.GET.get('search')
        if not search_keyword:
            coworks = models.Cowork.objects.get_coworks_list(**{})
        else:
            coworks = models.Cowork.objects.get_coworks_list_search(search_keyword)
        serializer = serializers.CoworksListSerializer(coworks, many=True)
        cowork_chunks = [serializer.data[x:x + 4] for x in range(0, len(serializer.data), 4)]

        context = {
            'data': cowork_chunks,
            'city_slug': None,
            # 'cities': utils.get_locations()
        }

        return render(request, template_name=self.template_name, context=context)


class CoworksDetails(APIView):
    """Coworks details page"""
    template_name = 'cowork-details.html'

    def get(self, request, country, city, slug):
        """
        Args:
            request:

        Returns:
        """
        cowork = models.Cowork.objects.get_cowork_by_slug(slug)
        serializer = serializers.CoworksDetailSerializer(cowork)
        similar_coworks = models.Cowork.objects.get_similar_coworks(cowork.locality)
        similar_coworks_serializer = serializers.SimilarCoworksDetailSerializer(similar_coworks, many=True)
        space_types = models.MembershipBenefits.objects.all()
        membership_serializer = serializers.MembershipBenefitSerializer(space_types, many=True)
        space_types = sorted(membership_serializer.data, key=utils.extract_membership_name)
        other_coworks_in_city = models.Cowork.objects.get_cowork_by_city(city, cowork)
        other_coworks_in_city_serializer = serializers.SimilarCoworksDetailSerializer(other_coworks_in_city, many=True)
        if serializer.is_valid:
            context = {
                'data': serializer.data,
                'similar_coworks': similar_coworks_serializer.data,
                'other_coworks_in_city': other_coworks_in_city_serializer.data,
                'space_types': space_types,
                'title': cowork.name + "| " + city + "| Book Online"
            }
            # return Response(context, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_200_OK)
            return render(request, template_name=self.template_name, context=context)
        return render(request, template_name=self.template_name, context={})