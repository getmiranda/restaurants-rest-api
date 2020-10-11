from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from restaurants_api import serializers
from restaurants_api import models


class RestaurantViewSet(viewsets.ModelViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.RestaurantSerializer
    queryset = models.Restaurant.objects.all()
