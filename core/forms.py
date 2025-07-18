from django import forms
from .models import Artista, Album, Cancion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Page

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'genero', 'nacionalidad', 'biografia']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'artista', 'anio', 'genero']


class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['titulo', 'album', 'duracion', 'letra']


class BusquedaCancionForm(forms.Form):
    titulo = forms.CharField(label='Título de la canción', max_length=100)



class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']