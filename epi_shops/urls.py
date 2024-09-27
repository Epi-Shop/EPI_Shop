from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page),
    path('login/', login),
    path('create_user/', create_user),
    path('shop/', shop),
]
