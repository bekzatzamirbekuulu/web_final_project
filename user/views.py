from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegistrateForm, LoginForm


class Login(LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'


class Logout(LogoutView):
    template_name = 'user/login.html'


class Registrate(CreateView):
    template_name = 'user/registrate.html'
    form_class = RegistrateForm
    success_url = reverse_lazy('user:login')

    def get_queryset(self):
        return User.objects.all()