<<<<<<< Updated upstream

from django.shortcuts import render
from ..models import Restaurant
=======
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
>>>>>>> Stashed changes

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})
