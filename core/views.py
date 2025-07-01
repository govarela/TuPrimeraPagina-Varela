from django.shortcuts import render, redirect
from .models import Artista, Album, Cancion
from .forms import ArtistaForm, AlbumForm, CancionForm, BusquedaCancionForm

def index(request):
    return render(request, 'core/index.html')

def agregar_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArtistaForm()
    return render(request, 'core/agregar_artista.html', {'form': form})

def agregar_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlbumForm()
    return render(request, 'core/agregar_album.html', {'form': form})

def agregar_cancion(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CancionForm()
    return render(request, 'core/agregar_cancion.html', {'form': form})

def buscar_cancion(request):
    canciones = []
    if request.method == 'GET':
        form = BusquedaCancionForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            canciones = Cancion.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaCancionForm()
    return render(request, 'core/buscar_cancion.html', {'form': form, 'canciones': canciones})