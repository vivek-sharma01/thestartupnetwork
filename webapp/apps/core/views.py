from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Index(APIView):
    """"""
    template_name = 'index.html'

    def get(self, request):
        """"""
        context = {}
        return render(request, template_name=self.template_name, context=context)