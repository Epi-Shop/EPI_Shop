from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView # Importe RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('epi_shops/', include('epi_shops.urls')),  # Inclui as URLs do app epi_shops
    path('login_app/', include('login_app.urls')), # Inclui as URLs do app login_app (autenticação)
    path('', RedirectView.as_view(url='login_app/')), # Redireciona para /login_app/
]