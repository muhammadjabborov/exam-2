from django.db import models
from django.utils import timezone


class VerificationCode(models.Model):
    phone_number = models.CharField(max_length=20)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Verification Code '
        verbose_name_plural = 'Verification Code'
        
