from datetime import date
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from monografias.forms import MonografiaForm
from . models import Monografias
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
def index(request):
    if request.method == 'POST':
        dados = request.POST.copy()
        inicio = int(dados('ano_inicial'))
        fim = int(dados('ano_final'))
        monografias = Monografias.objects.filter(dat_range=(date(inicio,1,1), date(fim,12,31)))
    else:
        monografias = Monografias.objects.all()
    
    context = {
        'lista': monografias
    }
    return render(request, 'monografias.html', context)

def detalhes(request,pk):
    print("Primary Key {}".format(pk))
    try:
        monografias = Monografias.objects.filter(pk=pk)
        print(monografias.values())
    
    except monografias.DoesNotExist:
        raise Http404('Monografia não existe')
    
    context = {
        'monografias':monografias
    }
    return render(request,'detalhes.html',context)


class CriarMonografia( CreateView):
    model = Monografias
    form_class = MonografiaForm

    template_name = 'add_monografia.html'
    success_url = reverse_lazy('index')

class EditarMonografia(UpdateView):
    model = Monografias
    form_class = MonografiaForm
    template_name = 'edit_monografia.html'
    success_url = reverse_lazy('index')

class DeletarMonografia(DeleteView):
    model = Monografias
    template_name = 'delete_monografia.html'
    success_url = reverse_lazy('index')