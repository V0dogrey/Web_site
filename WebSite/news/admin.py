from django.contrib import admin
from .models import Articles, CommentsList

# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'anons')
    list_display_links = ('title', 'id')
    search_fields = ('id', 'title', 'news_text')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_id', 'user_name', 'text')
    list_display_links = ('id', 'news_id', 'user_name', 'text')
    search_fields = ('user_name', 'text')

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(CommentsList, CommentsAdmin)