from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import RedirectView, View
from django.views.generic.edit import FormView

from giftline.mixins import AnonymousRequiredMixin, LoginRequiredMixin
from .forms import IndexForm, CrearIntercambioForm
from .models import Intercambio, Lista


class IndexView(AnonymousRequiredMixin, FormView):
    template_name = 'intercambios/index.html'
    form_class = IndexForm


class HomeView(LoginRequiredMixin, RedirectView):
    permanent = True

    def get_redirect_url(self):
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

    def get_context_data(self, **kwargs):
        context = super(IntercambioDetailView, self).get_context_data(**kwargs)
        context['admins'] = User.objects.filter(lista__intercambio=self.object, lista__is_admin=True)
        return context


class CrearIntercambioView(LoginRequiredMixin, View):
    def get(self, request):
        data = {'nombre': request.GET.get('nombre', '')}
        form = CrearIntercambioForm(initial=data)
        return render(request, 'intercambios/crear.html', {'form': form})

    def post(self, request):
        form = CrearIntercambioForm(request.POST)
        if form.is_valid():
            intercambio_id = self.iniciar_intercambio(request.user, form)
            return HttpResponseRedirect(reverse('app:invitar', args=(intercambio_id,)))
        return render(request, 'intercambios/crear.html', {'form': form})

    @staticmethod
    def iniciar_intercambio(user, form):
        nombre = form.cleaned_data['nombre']
        descripcion = form.cleaned_data['descripcion']
        intercambio = Intercambio(nombre=nombre, descripcion=descripcion)
        intercambio.save()
        # El creador del intercambio debe ser miembro y administrador:
        lista = Lista(user=user, intercambio=intercambio, is_admin=True)
        lista.save()
        return intercambio.id


@login_required
def invitar(request, pk):
    return render(request, 'intercambios/invitar.html')


class InvitarIntercambioView(LoginRequiredMixin, FormView):
    template_name = 'intercambios/invitar.html'
