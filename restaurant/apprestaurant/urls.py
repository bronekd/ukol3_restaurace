
from django.urls import path
from .views import *

urlpatterns = [
    path("res/", Restaurant.as_view(), name='restaurant'),
]
