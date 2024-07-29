
from django.urls import path
from .views import *
from .views.listrestaurant import RestaurantListView
from .views.createrestaurant import RestaurantCreateView
from .views.updaterestaurant import RestaurantUpdateView
from .views.deleterestaurant import RestaurantDeleteView

urlpatterns = [
    path("list/", RestaurantListView.as_view(), name='restaurant_list'),
    path("create/", RestaurantCreateView.as_view(), name='restaurant_create'),
    path('update/<int:pk>/', RestaurantUpdateView.as_view(), name='restaurant_update'),
    path('delete/<int:pk>/', RestaurantDeleteView.as_view(), name='delete_restaurant'),
]

