from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
  # Certifique-se de ter o template 'home.html'
def some_view(request):
    from .models import SomeModel 
