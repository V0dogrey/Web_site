from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class UserPrifile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return str('Профиль пользователья: ' + str(self.user.username))

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"