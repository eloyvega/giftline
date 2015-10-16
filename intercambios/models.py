from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Intercambio(models.Model):
    nombre = models.CharField(max_length=255, )
    status = models.BooleanField(default=True, )
    descripcion = models.TextField(blank=True)
    participantes = models.ManyToManyField(User,)