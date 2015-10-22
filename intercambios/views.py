from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings

from .forms import HomeForm
from .models import Intercambio


@user_passes_test(lambda user: not user.username, login_url=settings.HOME_URL, redirect_field_name=None)
def index(request):
    form = HomeForm()
    return render(request, 'intercambios/index.html', {'form': form})

@login_required
def home(request):
    intercambio = Intercambio.objects.filter(participantes__id=request.user.id)
    if len(intercambio) == 1:
        return HttpResponseRedirect(reverse('app:intercambio', args=(intercambio[0].id,)))
    else:
        return HttpResponseRedirect(reverse('app:intercambios'))

@login_required
def intercambios(request):
    return render(request, 'intercambios/intercambios.html')

@login_required
def intercambio(request, id):
    return render(request, 'intercambios/intercambio.html')
