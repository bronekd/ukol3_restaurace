from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView
from ..models import Restaurant
from ..forms import RestaurantForm

class RestaurantUpdateView(UpdateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'edit_restaurant.html'
    success_url = reverse_lazy('restaurant_list')
