from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),  # Adicione uma rota de exemplo, como 'index'
]
