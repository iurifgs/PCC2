from django.urls import path
from . import views

urlpatterns = [
    path('', views.readall, name='index'),  # Rota para a página inicial
    path('create/', views.create, name='Criar'),
    path('read/<int:id_animal>/', views.read, name='Ler'),  # Rota para os detalhes do animal
    path('update/<int:id_animal>/', views.update, name='Atualizar'),
    path('delete/<int:id_animal>/', views.delete, name='Deletar'),  # Rota para deletar um animal
    path('delete/confirm/<int:id_animal>/', views.confirmdelete, name='pet_confirm_delete'),
    path('register/', views.register, name='register'),  # Rota para o registro de usuário
    path('user_index/', views.user_index, name='user_index'),  # Rota para a página de usuário comum
    path('user_detail/<int:animal_id>/', views.user_detail, name='user_detail'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Rota para o painel de administração
    path('search/', views.search_animals, name='search_animals'),
    path('adoption-info/', views.adoption_info, name='adoption_info'),
]