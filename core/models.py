from django.db import models

class Auto(models.Model):
    modelo = models.CharField(max_length=100)  # Campo string de 100 caracteres
    año = models.IntegerField()  # Campo entero
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)  # Campo string de 30 caracteres
    apellido = models.CharField(max_length=30)  # Campo string de 30 caracteres
    email = models.EmailField()  # Campo de email

class Carrera(models.Model):
    carrera = models.CharField(max_length=30)  # Campo string de 30 caractere
    creditos = models.IntegerField()  # Campo entero
    fechaDeInicio = models.DateField()  # Campo de fecha

class Garantia(models.Model):
    nombre = models.CharField(max_length=100)  # Campo string de 100 caracteres
    email = models.EmailField()  # Campo de email
    telefono = models.IntegerField()  # Campo entero
    parentezco = models.BooleanField()  # Campo booleano
