from django.urls import path, include

from rest_framework.routers import DefaultRouter

from restaurants_api import views

router = DefaultRouter()
router.register('restaurants', views.RestaurantViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('utils/import-data/', views.import_data, name='utils-import-data'),
]