from django import forms

from .models import Intercambio


class IndexForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50,
                             widget=forms.TextInput(attrs={'placeholder': 'Nombre de intercambio'}))


class CrearIntercambioForm(forms.ModelForm):
    def crear_lista(self):
        pass

    class Meta:
        model = Intercambio
        fields = ['nombre', 'descripcion', ]
