from django.shortcuts import render

from .forms import HomeForm

def home(request):
    form = HomeForm()
    return render(request, 'intercambios/home.html', {'form':form})
