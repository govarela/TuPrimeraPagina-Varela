from django.shortcuts import render, redirect
from .models import Artista, Album, Cancion
from .forms import ArtistaForm, AlbumForm, CancionForm, BusquedaCancionForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from core.forms import RegistroForm
from django.contrib import messages
from .models import Page
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

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




def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # cambia por tu vista principal
    else:
        form = RegistroForm()
    return render(request, 'core/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

class PageListView(ListView):
    model = Page
    template_name = 'core/page_list.html'
    context_object_name = 'pages'

class PageDetailView(DetailView):
    model = Page
    template_name = 'core/page_detail.html'
    context_object_name = 'page'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'core/page_form.html'
    success_url = '/pages/'


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'core/page_form.html'
    success_url = reverse_lazy('page_list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'core/page_confirm_delete.html'
    success_url = reverse_lazy('page_list')