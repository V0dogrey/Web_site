from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def users(request):
    content = {
        'title': 'Users',
        'body': 'Hello User!',
    }
    return render(request, 'main/index.html', context=content)

def register(request):
    content = {
        'title': 'Users',
        'body': 'Hello User!',
    }
    return render(request, 'main/index.html', context=content)

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registration'
        return context