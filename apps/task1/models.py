from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken

from apps.common.models import BaseModel
from apps.task1.user_manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(max_length=32, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    birthday = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {"refresh": str(refresh), "access": str(refresh.access_token)}
