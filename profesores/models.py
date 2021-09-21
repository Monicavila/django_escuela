from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=300)
    correo = models.EmailField(null=True)
    contrato = models.CharField(max_length=300)