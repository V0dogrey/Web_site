from django.contrib import admin
from .models import Articles, CommentsList

# Register your models here.

admin.site.register(Articles)
admin.site.register(CommentsList)