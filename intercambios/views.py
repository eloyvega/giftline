from django.shortcuts import render

def home(request):
    return render(request, 'intercambios/home.html')
