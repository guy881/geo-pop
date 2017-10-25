from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255, verbose_name="Adres email")
    first_name = models.CharField(max_length=64, verbose_name="Imię")
    last_name = models.CharField(max_length=64, verbose_name="Nazwisko")
    is_active = models.BooleanField(default=False, verbose_name="Aktywny")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")
    is_staff = models.BooleanField(default=False, verbose_name="Członek zespołu")

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)
