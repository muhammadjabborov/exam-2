from django_filters import rest_framework as filters
from .models import Vacancy

from django.db.models import Q


class VacancyListFilter(filters.FilterSet):
    salary = filters.NumberFilter(method='filter_salary')

    class Meta:
        model = Vacancy
        fields = ['salary_from', 'salary_to', 'salary']

    def filter_salary(self, queryset, name, data):
        return queryset.filter(Q(salary_from__gte=data, salary_to__lte=data) | Q(salary=data))
