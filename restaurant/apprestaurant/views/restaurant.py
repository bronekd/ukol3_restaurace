from django.views.generic import TemplateView


class Restaurant(TemplateView):
    template_name = 'restaurant.html'