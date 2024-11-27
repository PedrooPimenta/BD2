from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Adicione uma rota de exemplo, como 'index'
    path('adicionar/', views.adicionar,name='adicionar'),
    path('criar/', views.CriarEquipe.as_view(), name='adicionar_equipe'),
    path('editar/<int:pk>/', views.EditarEquipe.as_view(), name='editar_equipe'),
    path('deletar/<int:pk>/', views.DeletarEquipe.as_view(), name='deletar_equipe'),
]