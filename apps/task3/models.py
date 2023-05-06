from django.db import models

from apps.common.models import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    marja = models.DecimalField(max_digits=10, decimal_places=2)
    package_code = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.title
