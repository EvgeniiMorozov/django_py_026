from re import IGNORECASE

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import RegexValidator, EmailValidator

from PIL import Image
from unidecode import unidecode


class MaxResolutionErrorException(Exception):
    pass


class MaxSizeErrorException(Exception):
    pass


# Кастомный валидатор на размер загружаемого файла
# "https://overcoder.net/q/17064/django-%D0%BE%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%80%D0%B0-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0"
def file_size(value):
    if value.size > User.MAX_PHOTO_SIZE:
        raise MaxSizeErrorException("Размер файла фотографии больше допустимого размера!")


class User(models.Model):
    MAX_PHOTO_RESOLUTION = (800, 800)
    MAX_PHOTO_SIZE = 3145728
    # Словарь с валидаторами
    VALIDATORS = {
        "regex": RegexValidator(
            regex=r"^[a-zа-я]", message="Имя|Фамилия должно начинаться с только с буквы!", code="invalid", flags=IGNORECASE
        ),
        "email": EmailValidator(
            message="Введите корректный email",
            whitelist=["my_domain", "my_host"],
        ),
    }

    first_name = models.CharField(max_length=30, verbose_name="Имя", validators=[VALIDATORS["regex"]])
    last_name = models.CharField(max_length=45, verbose_name="Фамилия", validators=[VALIDATORS["regex"]])
    email = models.EmailField(max_length=254, verbose_name="Электронная почта", validators=[VALIDATORS["email"]])
    photo = models.ImageField(upload_to="form_app/photos", verbose_name="Фотография", validators=[file_size])
    slug = models.SlugField(max_length=80, verbose_name="SLUG", unique=True, db_index=True)

    def __str__(self):
        return f"Пользователь {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("form_app:user_detail", kwargs={"user_slug": self.slug})

    def save(self, *args, **kwargs):
        photo = self.photo
        photo_image = Image.open(photo)
        img_width, img_height = photo_image.size
        max_width, max_height = self.MAX_PHOTO_RESOLUTION

        if img_width > max_width or img_height > max_height:
            raise MaxResolutionErrorException("Разрешение фото больше максимального!")

        if not self.slug:
            string = str(self.first_name) + "-" + str(self.last_name)
            self.slug = slugify(unidecode(string))

        super(User, self).save(*args, **kwargs)
