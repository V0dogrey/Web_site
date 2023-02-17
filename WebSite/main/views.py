from django.shortcuts import render

# Create your views here.
def index(request):
    content = {
        'title': 'Main Page',
        'body': 'Hello World!',
    }
    return render(request, 'main/index.html', context=content)