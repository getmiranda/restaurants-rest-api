from rest_framework import serializers

from restaurants_api import models


class RestaurantSerializer(serializers.ModelSerializer):
    """Serializes a restaurant object"""

    class Meta:
        model = models.Restaurant
        fields = '__all__'
