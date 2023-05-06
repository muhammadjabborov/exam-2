from rest_framework.generics import ListAPIView

from .serializers import ListVacancySerializer

from apps.task2.models import Vacancy
from apps.task2.filters import VacancyListFilter


class VacancyListAPIView(ListAPIView):
    serializer_class = ListVacancySerializer
    queryset = Vacancy.objects.all()
    filterset_class = VacancyListFilter
