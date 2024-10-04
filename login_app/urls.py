from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from . import views
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]