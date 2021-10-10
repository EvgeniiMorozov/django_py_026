from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import MyUser2Manager


# Create your models here.
class PostModel(models.Model):
    author = models.CharField("Автор статьи", max_length=30)
    title = models.CharField("Название статьи", max_length=50)
    slug = models.SlugField("URL", max_length=60, unique=True, db_index=True, null=True, blank=True)
    text = models.TextField("Текст статьи")
    image = models.ImageField("Картинка к посту", upload_to="img")  # pillow
    publish_date = models.DateTimeField("Время публикации", auto_now=True)
    is_published = models.BooleanField("Пост опубликован?", default=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категория")

    def get_absolute_url(self):
        return reverse("blog:show_post", kwargs={"post_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            string = str(self.title)
            self.slug = slugify(unidecode(string))
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-publish_date", "title"]


# статья -> statia
class Category(models.Model):
    name = models.CharField("Категория", max_length=30, unique=True)
    slug = models.SlugField("URL", max_length=30, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse("blog:show_cat", kwargs={"cat_slug": self.slug})

    def __str__(self):
        return self.name


# class MyUser(AbstractUser):
#     GENDERS = (
#         ('m', 'Мужчина'),
#         ('f', 'Женщина')
#     )
#     gender = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
#     fio = models.CharField('ФИО', max_length=50)


class MyUser2(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Электронная почта", max_length=50, unique=True, null=False, blank=False)
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUser2Manager()
