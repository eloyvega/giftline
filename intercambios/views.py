from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView, View
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect

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


# fixme Fuera de servicio hasta encontrar la implementacion correcta
class CrearIntercambioViewTODO(LoginRequiredMixin, FormView):
    template_name = 'intercambios/crear.html'
    form_class = CrearIntercambioForm

    def form_valid(self, form):
        form.crear_lista()
        return super(CrearIntercambioView, self).form_valid(form)

    def get_success_url(self):
        return reverse('app:invitar', args=(1,))


class CrearIntercambioView(LoginRequiredMixin, View):
    def get(self, request):
        form = CrearIntercambioForm()
        return render(request, 'intercambios/crear.html', {'form': form})

    def post(self, request):
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        i = Intercambio()
        i.nombre = nombre
        i.descripcion = descripcion
        i.save()
        return HttpResponseRedirect(reverse('app:invitar', args=(i.id,)))


@login_required
def invitar(request, pk):
    return render(request, 'intercambios/invitar.html')


class InvitarIntercambioView(LoginRequiredMixin, FormView):
    template_name = 'intercambios/invitar.html'
