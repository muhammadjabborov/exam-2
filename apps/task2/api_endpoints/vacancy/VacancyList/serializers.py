from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.task2.models import Vacancy


class ListVacancySerializer(ModelSerializer):
    company = serializers.StringRelatedField()

    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'company', 'salary_from', 'salary_to', 'salary')
