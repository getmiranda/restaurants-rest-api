import csv

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema

from restaurants_api import serializers
from restaurants_api import models


@swagger_auto_schema(
    operation_description="Importa los datos del archivo csv a la BD.", 
    methods=['post']
)
@api_view(['POST'])
def import_data(request):
    '''Importa los datos del archivo csv a la BD.'''
    restaurant_ids = [
        restaurant.id for restaurant in models.Restaurant.objects.all()
    ]

    with open('restaurantes.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] not in restaurant_ids:
                restaurant = models.Restaurant(
                    id=row['id'],
                    rating=row['rating'],
                    name=row['name'],
                    site=row['site'],
                    email=row['email'],
                    phone=row['phone'],
                    street=row['street'],
                    city=row['city'],
                    state=row['state'],
                    lat=row['lat'],
                    lng=row['lng']
                )
                restaurant.save()
    return Response(status=status.HTTP_200_OK)


class RestaurantViewSet(viewsets.ModelViewSet):
    """    
    retrieve:
    Return the given restaurant.

    list:
    Return a list of all the existing restaurants.

    create:
    Create a new restaurant instance.

    partial_update:
    Partially upgrade the given restaurant.

    update:
    Update the given restaurant.

    destroy:
    Delete the given restaurant.
    
    """
    serializer_class = serializers.RestaurantSerializer
    queryset = models.Restaurant.objects.all()
