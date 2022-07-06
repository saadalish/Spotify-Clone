from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, HttpResponseRedirect
from django.views import View

from .forms import SignUpForm


class SignupView(View):
    context = {}

    def get(self, request):
        form = SignUpForm()
        self.context = {
            'form': form
        }
        return render(request, 'users/signup.html', self.context)

    @staticmethod
    def post(request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login")


class UserLoginView(View):
    context = {}

    def get(self, request):
        form = AuthenticationForm()
        self.context = {
            'form': form
        }
        return render(request, 'users/signup.html', self.context)

    @staticmethod
    def post(request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            valid_user = authenticate(username=username, password=password)
            if valid_user is not None:
                login(request, valid_user)
                return HttpResponseRedirect("/")


class UserLogoutView(View):
    
    @staticmethod
    def get(request):
        logout(request)
        return HttpResponseRedirect("/")
