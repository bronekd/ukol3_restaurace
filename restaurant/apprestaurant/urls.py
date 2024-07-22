<<<<<<< Updated upstream
# restaurant/urls.py
=======
>>>>>>> Stashed changes
from django.urls import path
from .views import restaurant_list

urlpatterns = [
<<<<<<< Updated upstream
    path('', restaurant_list, name='restaurant_list'),
=======
    path("rest3/", Restaurant.as_view(), name='restaurant3'),
>>>>>>> Stashed changes
]
