from django.urls import path
from . import views
from .views import PageListView, PageDetailView
from .views import PageCreateView
from .views import PageUpdateView, PageDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar-artista/', views.agregar_artista, name='artista_create'),
    path('agregar-album/', views.agregar_album, name='album_create'),
    path('agregar-cancion/', views.agregar_cancion, name='cancion_create'),
    path('buscar/', views.buscar_cancion, name='buscar'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('pages/', PageListView.as_view(), name='page_list'),
    path('pages/<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('pages/create/', PageCreateView.as_view(), name='page_create'),
    path('pages/<int:pk>/edit/', PageUpdateView.as_view(), name='page_edit'),
    path('pages/<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),
]