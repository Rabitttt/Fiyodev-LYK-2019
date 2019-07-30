from django.contrib import auth
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.views.generic.list import ListView
from users.forms import UserRegisterForm, UserLoginForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login,logout
from django.views.generic import FormView, RedirectView
from .models import UserTable


class RegistrationView(FormView):
    form_class = UserRegisterForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    success_url = reverse_lazy("userlist")
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

class Logoutview(LogoutView):
    next_page = '/login'


class ListUser(ListView):
    template_name = "user_list.html"
    queryset = UserTable.objects.all()
    context_object_name = 'UserList'


class Home(TemplateView):
    template_name = 'users/home.html'
