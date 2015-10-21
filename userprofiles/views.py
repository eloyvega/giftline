from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def create_account(request):
    if request.method == 'POST':
        pass
    form = UserCreationForm()
    return render(request, 'userprofiles/create_account.html', {'form': form})


def signin(request):
    follow = request.GET.get('next', '/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(follow)
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    form = AuthenticationForm()
    return render(request, 'userprofiles/signin.html', {'form': form, 'redirect_to': follow})


def signout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)
