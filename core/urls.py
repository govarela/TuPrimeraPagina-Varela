from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.index, name='index'),
    path('agregar-artista/', views.agregar_artista, name='agregar_artista'),
    path('agregar-album/', views.agregar_album, name='agregar_album'),
    path('agregar-cancion/', views.agregar_cancion, name='agregar_cancion'),
    path('buscar-cancion/', views.buscar_cancion, name='buscar_cancion'),
]