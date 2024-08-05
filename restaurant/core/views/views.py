from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/loginv.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'

class Home(TemplateView):
    template_name = 'home.html'
