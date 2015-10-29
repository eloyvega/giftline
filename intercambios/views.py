from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.views.generic import ListView

from .forms import IndexForm
from .models import Intercambio
from giftline.mixins import AnonymousRequiredMixin, LoginRequiredMixin


class IndexView(AnonymousRequiredMixin, FormView):
    template_name = 'intercambios/index.html'
    form_class = IndexForm


class HomeView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        lista_intercambios = Intercambio.objects.filter(participantes__id=self.request.user.id)
        if len(lista_intercambios) == 1:
            return reverse('app:intercambio', args=(lista_intercambios[0].id,))
        else:
            return reverse('app:intercambios')


class IntercambiosListView(LoginRequiredMixin, ListView):
    model = Intercambio
    template_name = 'intercambios/intercambios.html'
    context_object_name = 'intercambios'

@login_required
def intercambios(request):
    return render(request, 'intercambios/intercambios.html')


@login_required
def intercambio(request, id):
    return render(request, 'intercambios/intercambio.html')
