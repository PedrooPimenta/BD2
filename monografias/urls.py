from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),  
    # Adicione uma rota de exemplo, como 'index'
    path('detalhes/<int:pk>/', views.detalhes, name='detalhes'),
    path('criar/', views.CriarMonografia.as_view(), name='criar_monografia'),
    path('editar/<int:pk>/', views.EditarMonografia.as_view(), name='editar_monografia'),
    path('deletar/<int:pk>/', views.DeletarMonografia.as_view(), name='deletar_monografia'),
]
