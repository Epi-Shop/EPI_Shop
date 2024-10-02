from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ... outras URLs do projeto
    path('admin/', admin.site.urls),
    path('', include('epi_shops.urls')),
    path('login/', include('login_app.urls')),  # Inclui as URLs da aplicação login_app
]