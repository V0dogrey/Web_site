from django.shortcuts import render

# Create your views here.
def news(request):
    content = {
        'title': 'News',
        'body': 'Hello World!',
    }
    return render(request, 'main/index.html', context=content)