from django.urls import path
from . import views

urlpatterns = [
<<<<<<< Updated upstream
    path('', views.index, name='index'),
    path('create_user/', views.create_user, name='create_user'), 
    path('login/', auth_views.LoginView.as_view(template_name='epi_shops/global/mtds_entrada/login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('cargos/', views.cargos, name='cargos'), 
    path('shop/', views.shop, name='shop'),
=======
    path('', views.EpiList.as_view(), name='epi_list'),
    path('<int:pk>/', views.EpiDetail.as_view(), name='epi_detail'),
    path('create/', views.EpiCreate.as_view(), name='epi_create'),
    path('<int:pk>/update/', views.EpiUpdate.as_view(), name='epi_update'),
    path('<int:pk>/delete/', views.EpiDelete.as_view(), name='epi_delete'),
    path('carrinho/adicionar/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('carrinho/', views.view_cart, name='view_cart'),
    path('carrinho/remover/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('carrinho/atualizar/<int:item_id>/', views.update_cart, name='update_cart'),
>>>>>>> Stashed changes
]