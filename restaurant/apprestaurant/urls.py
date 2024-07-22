# restaurant/urls.py
from django.urls import path
from .views import Restaurant

urlpatterns = [
    path('restaurant/', Restaurant, name='restaurant_list'),
]
