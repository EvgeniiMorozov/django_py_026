from django.db import models
from django.urls import reverse


class PostModel(models.Model):
    author = models.CharField(max_length=30, verbose_name='Автор статьи')
    title = models.CharField(max_length=45, verbose_name='Название статьи')
    text = models.TextField(verbose_name='Текст статьи')
    image = models.ImageField(verbose_name="Картинка", upload_to="photos/%Y/%m/%d/", null=True)
    publish_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации статьи')
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано?")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', kwargs={'id': self.pk})
