from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.News.as_view(), name='news'),
    path('<int:pk>', views.News_page.as_view(), name='news_id'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)