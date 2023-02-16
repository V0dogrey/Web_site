from django.shortcuts import render
from .models import Articles

# Create your views here.
def news(request):
    news = Articles.objects.order_by('-date')
    content = {
        'title': 'News',
        'news': news,
    }
    return render(request, 'news/main_news.html', context=content)