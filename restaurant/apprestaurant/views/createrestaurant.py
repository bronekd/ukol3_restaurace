from django.urls import reverse_lazy
from django.views.generic import CreateView
from ..models import Restaurant
from ..forms import RestaurantForm

class RestaurantCreateView(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'add_restaurant.html'
    success_url = reverse_lazy('restaurant_list')
