from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View, RedirectView

from giftline.mixins import AnonymousRequiredMixin


class SignupView(AnonymousRequiredMixin, View):
    def get(self, request):
        return self.signup(request)

    def post(self, request):
        return self.signup(request)

    def signup(self, request):
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
