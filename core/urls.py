from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar-artista/', views.agregar_artista, name='artista_create'),
    path('agregar-album/', views.agregar_album, name='album_create'),
    path('agregar-cancion/', views.agregar_cancion, name='cancion_create'),
    path('buscar/', views.buscar_cancion, name='buscar'),
]