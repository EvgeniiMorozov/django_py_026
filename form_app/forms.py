import re

from PIL import Image
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, EmailInput
from django.utils.safestring import mark_safe

from form_app.models import User


class UserRegistrationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields["photo"].help_text = mark_safe(
            "<div><span style='color:green;font-size:14px;'>Загружайте фото разрешением {} x {} и размером не более 3 Мб</span></div>".format(
                *User.MAX_PHOTO_RESOLUTION))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "photo"]
        widgets = {
            "first_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Имя пользователя"
            }),
            "last_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Фамилия пользователя"
            }),
            "email": EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Электронная почта"
            }),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        # Проверяем, что введеное имя на чинается с буквы
        if not re.match(r"^\w", first_name):
            raise ValidationError("Имя пользователя должна начинаться с буквы!")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        # Проверяем, что введеная фамилия на чинается с буквы
        if not re.match(r"^\w", last_name):
            raise ValidationError("Фамилия пользователя должна начинаться с буквы!")
        return last_name

    def clean_photo(self):
        photo = self.cleaned_data["photo"]
        img = Image.open(photo)
        max_width, max_height = User.MAX_PHOTO_RESOLUTION
        # Проверяем разрешение загружаемого фото
        if img.width > max_width or img.height > max_height:
            raise ValidationError("Разрешение фото больше максимального!")
        # Проверяем размер загружаемого фото
        if img.size > User.MAX_PHOTO_SIZE:
            raise ValidationError("Размер файла фотографии больше допустимого размера!")
        return photo