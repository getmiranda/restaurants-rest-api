from django.urls import path

from restaurants_api import views


urlpatterns = [
    path('restaurants-view', views.RestaurantApiView.as_view()),
]