from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View, RedirectView

from giftline.mixins import AnonymousRequiredMixin


class SignupView(AnonymousRequiredMixin, View):
    def get(self, request):
        return self.render_form(request)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return self.render_form(request)

    @staticmethod
    def render_form(request):
        form = UserCreationForm()
        return render(request, 'userprofiles/signup.html', {'form': form})


class SigninView(AnonymousRequiredMixin, View):
    def get(self, request):
        follow = self.get_next(request)
        form = AuthenticationForm()
        return render(request, 'userprofiles/signin.html', {'form': form, 'redirect_to': follow})

    def post(self, request):
        follow = self.get_next(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(follow)
            else:
                return HttpResponse('Inactive user.')
        else:
            form = AuthenticationForm()
            return render(request, 'userprofiles/signin.html', {
                'form': form,
                'redirect_to': follow,
                'error_message': 'Usuario o contraseña incorrecto',
            })

    @staticmethod
    def get_next(request):
        return request.GET.get('next', '/')


class SignoutView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self):
        logout(self.request)
        return reverse('index')
