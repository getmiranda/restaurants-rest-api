import csv

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema

from restaurants_api import serializers
from restaurants_api import models


@swagger_auto_schema(
    operation_description="Import data from csv file to DB.",
    methods=['post']
)
@api_view(['POST'])
def import_data(request):
    '''Import data from csv file to DB.'''
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


@swagger_auto_schema(
    operation_description="Delete data from DB.",
    methods=['post']
)
@api_view(['POST'])
def delete_data(request):
    '''Delete data from DB.'''
    models.Restaurant.objects.all().delete()
    return Response(status=status.HTTP_200_OK)


@swagger_auto_schema(
    operation_description="",
    methods=['GET']
)
@api_view(['GET'])
def statistics(request):
    ''''''
    # http://127.0.0.1:8000/restaurants/statistics/?latitude=x&longitude=y&radius=z

    return Response({
        'latitude': request.GET.get('latitude', ''),
        'longitude': request.GET.get('longitude', ''),
        'radius': request.GET.get('radius', ''),
        'count': 0,
        'avg': 0,
        'std': 0
    })


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
