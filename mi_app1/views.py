from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BodegaForm, EnologoForm, VinoForm
from .models import Bodega, Enologo, Vino
import os

def prueba(request):
    return HttpResponse("¡Vista de prueba funcionando!")

vista_de_prueba = prueba

print("CARGADO mi_app1/views.py DESDE:", os.path.abspath(__file__))

def lista_vinos(request):
    vinos = Vino.objects.select_related('bodega').all()
    return render(request, 'lista_vinos.html', {'vinos': vinos})

def crear_bodega(request):
    if request.method == 'POST':
        form = BodegaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_bodega')
    else:
        form = BodegaForm()
    return render(request, 'mi_app1/crear_bodega.html', {'form': form})

def crear_enologo(request):
    if request.method == 'POST':
        form = EnologoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_enologo')
    else:
        form = EnologoForm()
    return render(request, 'mi_app1/crear_enologo.html', {'form': form})

def crear_vino(request):
    if request.method == 'POST':
        form = VinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_vino')
    else:
        form = VinoForm()
    return render(request, 'mi_app1/crear_vino.html', {'form': form})

def buscar_vino(request):
    query = request.GET.get('nombre')
    vinos = None
    if query:
        vinos = Vino.objects.filter(nombre__icontains=query)
    return render(request, 'mi_app1/buscar_vino.html', {'vinos': vinos})
