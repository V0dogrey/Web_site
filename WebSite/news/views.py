from django.shortcuts import render
from .models import Articles, CommentsList
from  django.views.generic import DetailView


# Create your views here.

class News_page(DetailView):
    model = Articles
    template_name = 'news/news_page.html'
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pkk'] = self.object.pk
        context['comments'] = CommentsList.objects.filter(news_id=self.object.pk)
        return context








def news(request):
    news = Articles.objects.order_by('-date')
    content = {
        'title': 'News',
        'news': news,
    }
    return render(request, 'news/main_news.html', context=content)