from django.urls import path, include

from rest_framework.routers import DefaultRouter

from restaurants_api import views

router = DefaultRouter()
router.register('restaurants', views.RestaurantViewSet)


urlpatterns = [
    path('', include(router.urls)),
]