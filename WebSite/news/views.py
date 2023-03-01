from datetime import datetime

from django.shortcuts import render
from .models import Articles, CommentsList, reverse
from django.views.generic import DetailView
from .forms import AddCommentForm

from django.views.generic.edit import FormMixin
from django.http import HttpResponseForbidden


# Create your views here.

class News_page(FormMixin, DetailView):
    model = Articles
    template_name = 'news/news_page.html'
    context_object_name = "article"
    form_class = AddCommentForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = CommentsList.objects.filter(news_id=self.object.pk)
        context['form'] = self.get_form()
        return context

    def get_success_url(self):
        return reverse('news_id', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        # Assign the current post to the comment
        new_comment.date = datetime.now()
        new_comment.news_id = self.object
        # Save the comment to the database
        new_comment.save()
        return super(News_page, self).form_valid(form)


def news(request):
    news = Articles.objects.order_by('-date')
    content = {
        'title': 'News',
        'news': news,
    }
    return render(request, 'news/main_news.html', context=content)