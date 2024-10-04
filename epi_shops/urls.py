from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('epis/', views.EpiList.as_view(), name='epi_list'),  
    path('epis/<int:pk>/', views.EpiDetail.as_view(), name='epi_detail'),  
    path('epis/create/', views.EpiCreate.as_view(), name='epi_create'),  
    path('epis/<int:pk>/update/', views.EpiUpdate.as_view(), name='epi_update'),  
    path('epis/<int:pk>/delete/', views.EpiDelete.as_view(), name='epi_delete'), 
    path('carrinho/adicionar/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('carrinho/', views.view_cart, name='view_cart'),
    path('carrinho/remover/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('carrinho/atualizar/<int:item_id>/', views.update_cart, name='update_cart'),
]