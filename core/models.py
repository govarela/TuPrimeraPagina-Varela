from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    biografia = models.TextField()

    def __str__(self):
        return self.nombre


class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)  # Nombre del artista (sin FK)
    anio = models.IntegerField()
    genero = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.titulo} ({self.anio})"


class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    album = models.CharField(max_length=100)  # Nombre del álbum (sin FK)
    duracion = models.CharField(max_length=10)  # Ej: "3:45"
    letra = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
    


class Page(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='pages/', blank=True, null=True)
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    cumpleaños = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

# Crear perfil automáticamente cuando se crea un usuario
@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
