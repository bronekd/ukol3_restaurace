from django.urls import reverse_lazy
from django.views.generic import DeleteView
from ..models import Restaurant

class RestaurantDeleteView(DeleteView):
    model = Restaurant
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('restaurant_list')

