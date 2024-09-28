from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user/', views.create_user, name='create_user'), 
    path('login/', auth_views.LoginView.as_view(template_name='epi_shops/global/mtds_entrada/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('cargos/', views.cargos, name='cargos'), 
    path('shop/', views.shop, name='shop'),
]