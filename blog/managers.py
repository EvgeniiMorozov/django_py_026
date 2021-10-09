from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class MyUser2Manager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Электронная почта должна обязательна быть!")

        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Суперпользователь должен быть с правами суперпользователя!")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперпользователь должен быть с правами просмотра админки!")
        if extra_fields.get("is_active") is not True:
            raise ValueError("Суперпользователь должен быть активирован!")
        return self.create_user(email, password, **extra_fields)
