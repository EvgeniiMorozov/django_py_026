from re import IGNORECASE
from PIL import Image
from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator, EmailValidator, FileExtensionValidator


class MaxResolutionErrorException(Exception):
    pass


class MaxSizeErrorException(Exception):
    pass


class User(models.Model):
    MAX_PHOTO_RESOLUTION = (800, 800)
    MAX_PHOTO_SIZE = 3145728
    VALIDATORS = {
        "regex": RegexValidator(
            regex=r"^\w", message="Имя|Фамилия должно начинаться с только с буквы!", code="invalid", flags=IGNORECASE
        ),
        "email": EmailValidator(
            message="Разрешённые почтовые домены: mail.ru, yandex.ru, gmail.com",
            allowlist=["mail.ru", "yandex.ru", "gmail.com"],
        ),
    }

    first_name = models.CharField(max_length=30, verbose_name="Имя", validators=[VALIDATORS["regex"]])
    last_name = models.CharField(max_length=45, verbose_name="Фамилия", validators=[VALIDATORS["regex"]])
    email = models.EmailField(max_length=254, verbose_name="Электронная почта", validators=VALIDATORS["email"])
    photo = models.ImageField(upload_to="form_app/photos", verbose_name="Фотография")
    slug = models.SlugField(max_length=80, verbose_name="SLUG", unique=True, db_index=True)

    def __str__(self):
        return f"Пользователь {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("form_app:users", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        photo = self.photo
        img = Image.open(photo)
        max_width, max_height = self.MAX_PHOTO_RESOLUTION

        if img.width > max_width or img.height > max_height:
            raise MaxResolutionErrorException("Разрешение фото больше максимального!")

        if img.size > User.MAX_PHOTO_SIZE:
            raise MaxSizeErrorException("Размер файла фотографии больше допустимого размера!")

        super(User, self).save(*args, **kwargs)
