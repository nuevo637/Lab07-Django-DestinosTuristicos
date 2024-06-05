from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *

#LISTAR DESTINOS
def listar_destino(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'listar.html', {'destinos': destinos})

#CREAR DESTINOS
def crear_destino(request):
    if request.method == 'POST':
        form = DestinosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("El destino ha sido creado correctamente") 
    else:
        form = DestinosForm()
    return render(request, 'crear.html', {'form': form})

#EDITAR DESTINO
def seleccionar_y_editar_destino(request, pk=None):
    if pk:
        destino = get_object_or_404(DestinosTuristicos, pk=pk)
        if request.method == 'POST':
            form = DestinosForm(request.POST, request.FILES, instance=destino)
            if form.is_valid():
                form.save()
                return HttpResponse("El destino ha sido actualizado correctamente")
        else:
            form = DestinosForm(instance=destino)
    else:
        form = None
    
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'editar.html', {'destinos': destinos, 'form': form, 'selected_destino': pk})

#ELIMINAR DESTINO
def eliminar_destino(request):
    if request.method == 'POST':
        nombre_ciudad = request.POST.get('nombreCiudad')
        destino = get_object_or_404(DestinosTuristicos, nombreCiudad=nombre_ciudad)
        destino.delete()
        return HttpResponse("El destino ha sido eliminado correctamente")  
    else:
        destinos = DestinosTuristicos.objects.all()
        return render(request, 'eliminar.html', {'destinos': destinos})