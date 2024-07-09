from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('user_index/', views.user_index, name='user_index'),
    path('index/', views.index, name='index'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Adicione esta linha
]