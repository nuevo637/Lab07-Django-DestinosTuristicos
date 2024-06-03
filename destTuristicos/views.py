from django.shortcuts import render, redirect
from .forms import *
from .models import *

#LISTAR DESTINOS
def listar_destino(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'listar.html', {'destinos': destinos})

#CREAR DESTINOS
def crear_destino(request):
    if request.method == 'POST':
        form = DestinosForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DestinosForm()
    return render(request, 'crear.html', {'form': form})