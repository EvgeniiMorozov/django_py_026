from PIL import Image
from django.db import models


class MaxResolutionErrorException(Exception):
    pass


class MaxSizeErrorException(Exception):
    pass


class User(models.Model):
    MAX_PHOTO_RESOLUTION = (800, 800)
    MAX_PHOTO_SIZE = 3145728

    first_name = models.CharField(max_length=30, verbose_name="Имя", blank=False, null=False)
    last_name = models.CharField(max_length=45, verbose_name="Фамилия", blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False, verbose_name="Электронная почта")
    photo = models.ImageField(upload_to="form_app/photos", null=False, verbose_name="Фотография")
    slug = models.SlugField(max_length=80, verbose_name="SLUG", unique=True)

    def __str__(self):
        return f"Пользователь {self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        photo = self.photo
        img = Image.open(photo)
        max_width, max_height = self.MAX_PHOTO_RESOLUTION

        if img.width > max_width or img.height > max_height:
            raise MaxResolutionErrorException("Разрешение фото больше максимального!")

        if img.size > User.MAX_PHOTO_SIZE:
            raise MaxSizeErrorException("Размер файла фотографии больше допустимого размера!")

        super(User, self).save(*args, **kwargs)