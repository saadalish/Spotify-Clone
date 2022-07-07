from django.views import generic

from .forms import SignUpForm


class SignupView(generic.CreateView):
    form_class = SignUpForm
    success_url = '/'
    template_name = 'users/signup.html'
