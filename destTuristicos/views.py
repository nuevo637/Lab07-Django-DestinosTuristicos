from django.shortcuts import render
from .models import DestinosTuristicos

# Create your views here.
def destinos(request):
    
    
    
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'index.html', {'destinos': destinos})