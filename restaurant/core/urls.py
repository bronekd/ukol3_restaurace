from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from .views.home import Home



urlpatterns = [
    path("", Home.as_view(), name="home"),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

