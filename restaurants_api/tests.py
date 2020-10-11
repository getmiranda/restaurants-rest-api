from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from restaurants_api.models import Restaurant
from restaurants_api.serializers import RestaurantSerializer


def create_restaurant(**params):
    """Helper function to create new restaurant"""
    return Restaurant.objects.create(**params)


class RestaurantTest(TestCase):
    """Test the restaurants API"""

    def setUp(self):
        self.client = APIClient()
        self.payload = {
            'id': '123456789',
            'rating': 4,
            'name': 'Test Name',
            'site': 'Test Site',
            'email': 'user@example.com',
            'phone': '123456789',
            'street': 'Test Street',
            'city': 'Test City',
            'state': 'Test State',
            'lat': 10.0,
            'lng': -10.0
        }

    def test_create_restaurant_success(self):
        """Test creating using with a valid payload is successful"""
        res = self.client.post('/api/restaurants/', self.payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_restaurant_exists(self):
        """Test creating a restaurant that already exists fails"""
        create_restaurant(**self.payload)
        res = self.client.post('/api/restaurants/', self.payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_any_missing_field(self):
        """Test that name and email are required"""
        payload = {
            'id': '123456789',
            'rating': 4,
            'site': 'Test Site',
            'phone': '123456789',
            'street': 'Test Street',
            'city': 'Test City',
            'state': 'Test State',
            'lat': 10.0,
            'lng': -10.0
        }
        res = self.client.post('/api/restaurants/', payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_restaurant_list(self):
        """Test retrieving a list of restaurants"""
        payload_2 = {
            'id': '987654321',
            'rating': 4,
            'name': 'Test Name',
            'site': 'Test Site',
            'email': 'user2@example.com',
            'phone': '987654321',
            'street': 'Test Street',
            'city': 'Test City',
            'state': 'Test State',
            'lat': 10.0,
            'lng': -10.0
        }
        create_restaurant(**self.payload)
        create_restaurant(**payload_2)

        res = self.client.get('/api/restaurants/')

        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_restaurant_delete_success(self):
        """Test deleting a restaurant that already exists"""
        create_restaurant(**self.payload)
        res = self.client.delete(
            '/api/restaurants/{}/'.format(self.payload['id'])
        )

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_restaurant_delete_failed(self):
        """Test deleting a restaurant that already exists failed"""
        res = self.client.delete('/api/restaurants/123456789/')

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_restaurant_update_success(self):
        '''Test updating a restaurant than already exist'''
        payload_2 = {
            'id': '987654321',
            'rating': 4,
            'name': 'Test Name',
            'site': 'Test Site',
            'email': 'user2@example.com',
            'phone': '987654321',
            'street': 'Test Street',
            'city': 'Test City',
            'state': 'Test State',
            'lat': 10.0,
            'lng': -10.0
        }
        restaurant = create_restaurant(**self.payload)
        res = self.client.put(
            '/api/restaurants/{}/'.format(self.payload['id']),
            data=payload_2
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertNotEqual(res.data['email'], restaurant.email)
