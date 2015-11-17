from django.db import models
from django.contrib.auth.models import User


class Intercambio(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    fecha = models.DateTimeField(blank=True, null=True)
    publico = models.BooleanField(default=False)
    eliminado = models.BooleanField(default=False)
    miembros = models.ManyToManyField(User, through='Participante')

    def __str__(self):
        return self.nombre


class Participante(models.Model):
    user = models.ForeignKey(User)
    intercambio = models.ForeignKey(Intercambio)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return 'Participante de %s' % self.intercambio.nombre
