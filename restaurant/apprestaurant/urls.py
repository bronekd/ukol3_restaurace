
from django.urls import path
from .views import *

urlpatterns = [
    path("list/", RestaurantListView.as_view(), name='restaurant_list'),
    path("create/", RestaurantCreateView.as_view(), name='restaurant_create'),
    path("update/", RestaurantUpdateView.as_view(), name='restaurant_update'),
]
