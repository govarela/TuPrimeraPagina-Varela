from django import forms
from .models import Artista, Album, Cancion

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