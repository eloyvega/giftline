from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def create_account(request):
    if request.method == 'POST':
        pass
    form = UserCreationForm()
    return render(request, 'userprofiles/create_account.html', {'form':form})