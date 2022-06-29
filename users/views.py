from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, HttpResponseRedirect

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            valid_user = authenticate(username=username, password=password)
            if valid_user is not None:
                login(request, valid_user)
                return HttpResponseRedirect("/playlists/")
    else:
        form = AuthenticationForm()
    return render(request, 'users/user_login.html', {'form': form})

