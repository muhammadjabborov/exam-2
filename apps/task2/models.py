from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_company = models.CharField(max_length=100)
    legal_name_company = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name_company


class Vacancy(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, )
    title = models.CharField(max_length=100)
    salary_from = models.PositiveIntegerField(null=True, blank=True)
    salary_to = models.PositiveIntegerField(null=True, blank=True)
    salary = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
