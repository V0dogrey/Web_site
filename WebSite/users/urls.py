from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.users, name='users'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('logout/', views.logout_user, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)