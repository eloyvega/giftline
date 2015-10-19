from django.db import models
from django.contrib.auth.models import User


class Intercambio(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    participantes = models.ManyToManyField(User, through='Lista')

    def __str__(self):
        return self.nombre


class Lista(models.Model):
    user = models.ForeignKey(User)
    intercambio = models.ForeignKey(Intercambio)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user

