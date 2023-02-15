from django.shortcuts import render
"""from django.http import HttpResponse"""

# Create your views here.
def index(requset):
    content = {
        'title': 'Main Page.',
        'body': 'Hello World!',
    }
    return render(requset, 'main/index.html', context=content)