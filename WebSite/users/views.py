from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.
def users(request):
    content = {
        'title': 'Users',
        'body': 'Hello User!',
    }
    return render(request, 'main/index.html', context=content)

class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registration'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')

class UserLogin(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    def get_context_data(self,  *, object_list=None, **kwargs):
        context = super(UserLogin, self).get_context_data(**kwargs)
        context['title'] = 'Login'
        return context
    def get_success_url(self):
        return reverse_lazy('profile')

class UserProfile(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'User'

    def get_object(self):
        return get_object_or_404(User, username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data()
        return context


def logout_user(request):
    logout(request)
    return redirect('news')