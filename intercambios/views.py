from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.views.generic import ListView, DetailView

from .forms import IndexForm, CrearIntercambioForm
from .models import Intercambio
from giftline.mixins import AnonymousRequiredMixin, LoginRequiredMixin


class IndexView(AnonymousRequiredMixin, FormView):
    template_name = 'intercambios/index.html'
    form_class = IndexForm


class HomeView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        num_intercambios = Intercambio.objects.filter(participantes__id=self.request.user.id).count()
        if num_intercambios == 1:
            return reverse('app:intercambio',
                           args=(Intercambio.objects.get(participantes__id=self.request.user.id).id,))
        else:
            return reverse('app:intercambios')


class IntercambiosListView(LoginRequiredMixin, ListView):
    template_name = 'intercambios/intercambios.html'
    context_object_name = 'intercambios'

    def get_queryset(self):
        return Intercambio.objects.filter(participantes__id=self.request.user.id)


class IntercambioDetailView(LoginRequiredMixin, DetailView):
    model = Intercambio
    template_name = 'intercambios/intercambio.html'
    context_object_name = 'intercambio'


class CrearIntercambioView(LoginRequiredMixin, FormView):
    template_name = 'intercambios/crear.html'
    form_class = CrearIntercambioForm
