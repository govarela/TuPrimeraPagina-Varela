from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Artista, Album, Cancion
from .forms import ArtistaForm, AlbumForm, CancionForm, BusquedaCancionForm

def index(request):
    return render(request,'core/index.html')


def home(request):
    return render(request, 'home.html')


def agregar_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArtistaForm()
    return render(request, 'agregar_artista.html', {'form': form})


def agregar_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm()
    return render(request, 'agregar_album.html', {'form': form})


def agregar_cancion(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CancionForm()
    return render(request, 'agregar_cancion.html', {'form': form})


def buscar_cancion(request):
    canciones = []
    if request.method == 'GET':
        form = BusquedaCancionForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            canciones = Cancion.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaCancionForm()
    return render(request, 'buscar_cancion.html', {'form': form, 'canciones': canciones})
