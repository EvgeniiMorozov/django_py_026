from django.db import models


class PostModel(models.Model):
    author = models.CharField(max_length=30, verbose_name='Автор статьи')
    title = models.CharField(max_length=45, verbose_name='Название статьи')
    text = models.TextField(verbose_name='Текст статьи')
    publish_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации статьи')

    def __str__(self):
        return self.title
