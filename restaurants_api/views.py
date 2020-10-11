from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from restaurants_api import serializers
from restaurants_api import models


class RestaurantApiView(APIView):
    """Restaurant API View"""
    # serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of a function features"""
        an_apiview = [
            'Uses HTTP methods as a function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


