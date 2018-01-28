from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models, serializers


class EnterpreneurIndex(APIView):
    """"""
    template_name = 'index.html'

    def get(self, request):
        """"""
        context = {
            'title': 'Enterpreneur'
        }
        return render(request, template_name=self.template_name, context=context)


class StartUpIndex(APIView):
    """"""
    template_name = 'index.html'

    def get(self, request):
        """"""
        context = {
            'title': 'StartUp'
        }
        return render(request, template_name=self.template_name, context=context)



class Subscribe(APIView):
    """"""
    template_name = 'contact.html'

    # @csrf_protect
    def post(self, request):
        """"""
        email = request.data.get('email')
        try:
            models.Subscribe.objects.create(**{'email': email})
            return Response({'message': 'success'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'error'}, status=status.HTTP_400_BAD_REQUEST)


class ContactUs(APIView):
    """"""
    template_name = 'contact-us.html'

    def get(self, request):
        """"""
        context = {
            'title': 'Contact Us'
        }
        return render(request, template_name=self.template_name, context=context)


class ContactUsForm(APIView):
    """"""

    def post(self, request):
        """Contact us form details"""

        serializer = serializers.ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success'}, status=status.HTTP_200_OK)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)