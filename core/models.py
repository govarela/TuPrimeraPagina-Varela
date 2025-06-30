from django.db import models

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
