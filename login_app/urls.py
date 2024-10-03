from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView 
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login_app/pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', CreateView.as_view(
        template_name='login_app/pages/register.html',
        form_class=UserCreationForm,
        success_url=reverse_lazy('login')
    ), name='register'),
]