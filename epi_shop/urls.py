from django.contrib import admin
from django.urls import path, include
from epi_shops import views as epi_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('epi_shops.urls')),  
]