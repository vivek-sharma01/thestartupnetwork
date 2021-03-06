from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models, serializers
from webapp.apps.coworks import models as cowork_models
from webapp.apps.coworks import utils as cowork_utils
from webapp.apps.coworks import constants as cowork_constant


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

        data = request.data
        cowork = None
        if 'cowork_slug' in request.data:
            cowork = cowork_models.Cowork.objects.get_cowork_by_slug(request.data['cowork_slug'])
            data['cowork_id'] = cowork.id

        serializer = serializers.ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if cowork_constant.CONTACT_US_MAIL_FUCTION_MAPPING.get(data['reason']):
                function_name = cowork_constant.CONTACT_US_MAIL_FUCTION_MAPPING.get(data['reason'])
                function = getattr(cowork_utils, function_name)
                function(data, cowork)
            else:
                cowork_utils.send_mail_to_cowork(data, cowork)
            if data['reason'] == 'membership enquiry':
                cowork_utils.send_mail_to_customer(data, cowork)
            return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)