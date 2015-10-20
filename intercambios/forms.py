from django import forms

class HomeForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50, widget=forms.TextInput(attrs={'placeholder':'Nombre de intercambio'}))