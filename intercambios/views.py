from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .forms import HomeForm


@user_passes_test(lambda user: not user.username, login_url='/home', redirect_field_name=None)
def index(request):
    form = HomeForm()
    return render(request, 'intercambios/index.html', {'form': form})


@login_required
def home(request):
    return render(request, 'intercambios/home.html')