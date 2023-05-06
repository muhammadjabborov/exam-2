from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class CustomUserManager(BaseUserManager):

    def create_user(self, first_name, last_name, phone_number, password=None):
        user = self.model(phone_number=phone_number, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, phone_number, password=None):
        user = self.model(
            phone_number=phone_number, first_name=first_name, last_name=last_name, password=make_password(password)
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user
