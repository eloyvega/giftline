from django import forms

from .models import Intercambio


class IndexForm(forms.Form):
    intercambio = forms.CharField(label='Nombre', max_length=50,
                                  widget=forms.TextInput(attrs={'placeholder': 'Nombre de intercambio'}))


class CrearIntercambioForm(forms.ModelForm):

    class Meta:
        model = Intercambio
        fields = ['nombre', 'descripcion', ]
