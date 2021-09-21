from django.db import models

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=200)
    clave = models.CharField(max_length=18, unique=True)
    descripcion = models.TextField()