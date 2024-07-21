from django.views.generic import ListView



class Home(ListView):
    template_name = 'home.html'