from django.db import models

# Create your models here.
class Facultad(models.Model):
    nombre = models.CharField(max_length=200)
    campus = models.CharField(max_length=200)
    clave = models.IntegerField()