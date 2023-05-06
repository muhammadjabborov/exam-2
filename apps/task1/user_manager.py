from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, phone_number, password=None, defaults=None):
        if not username:
            raise ValueError("Username is required")

        if defaults is None:
            defaults = {}

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            **defaults
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, phone_number, password, defaults=None):
        if defaults is None:
            defaults = {}

        defaults.update({
            'is_staff': True,
            'is_superuser': True,
            'is_active': True
        })

        return self.create_user(username, first_name, last_name, phone_number, password, defaults=defaults)
