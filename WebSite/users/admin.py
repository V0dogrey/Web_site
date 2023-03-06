from django.contrib import admin
from .models import UserPrifile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user')
    list_display_links = ('user')
    search_fields = ('user')



admin.site.register(UserPrifile)