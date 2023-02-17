from django.shortcuts import render
from .models import Articles
from  django.views.generic import DetailView

# Create your views here.

class News_page(DetailView):
    model = Articles
    template_name = 'news/news_page.html'
    context_object_name = 'article'


def news(request):
    news = Articles.objects.order_by('-date')
    content = {
        'title': 'News',
        'news': news,
    }
    return render(request, 'news/main_news.html', context=content)