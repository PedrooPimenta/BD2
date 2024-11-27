from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipe
from .forms import EquipeForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.

def index(request):
    equipe = Equipe.objects.all()
    context = {
        'lista': equipe
    }
    return render(request, 'equipe.html', context)
  # Certifique-se de ter o template 'home.html'
def adicionar(request):
    if request.method == "POST":
        form = EquipeForm(request.POST)  # Passe os dados da solicitação para o formulário.
        if form.is_valid():
            post = form.save()
            post . save()
            form = EquipeForm()
            return render(request, 'adicionar_equipe.html', {'form': form})  # Fornecer o contexto adequado.
    else:
        form = EquipeForm()
    return render(request, 'adicionar_equipe.html', {'form': form})  # Certifique-se de fornecer o formulário, mesmo no ramo "else".


def some_view(request):
   from .models import SomeModel 

class CriarEquipe( CreateView):
    model = Equipe
    form_class = EquipeForm
    template_name = 'adicionar_equipe.html'
    success_url = reverse_lazy('index')

class EditarEquipe(UpdateView):
    model = Equipe
    form_class = EquipeForm
    template_name = 'editar_equipe.html'
    success_url = reverse_lazy('index')    

class DeletarEquipe(DeleteView):
    model = Equipe
    template_name = 'deletar_equipe.html'    
    success_url = reverse_lazy('index')