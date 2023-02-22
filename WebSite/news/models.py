from django.db import models

# Create your models here.



class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    news_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class CommentsList(models.Model):
    news_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
    user_name = models.CharField('Имя', max_length=50)
    text = models.TextField('Комментарий', max_length=500)
    date = models.DateTimeField('Дата')

    def __str__(self):
        return str(self.news_id) + ": Пользователь: "  + self.user_name + ": " + self.text


    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Кометарии"