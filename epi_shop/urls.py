from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
=======
<<<<<<< Updated upstream
from epi_shops import views as epi_views
=======
from django.views.generic import RedirectView
>>>>>>> Stashed changes
>>>>>>> development

urlpatterns = [
    # ... outras URLs do projeto
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('epi_shops.urls')),
    path('login/', include('login_app.urls')),  # Inclui as URLs da aplicação login_app
=======
<<<<<<< Updated upstream
    path('', include('epi_shops.urls')),  
=======
    path('', include('epi_shops.urls')),
    path('login/', include('login_app.urls')),  # Inclui as URLs da aplicação login_app
    path('admin/login/', RedirectView.as_view(url='/index/', permanent=False)),  # Custom redirect
>>>>>>> Stashed changes
>>>>>>> development
]