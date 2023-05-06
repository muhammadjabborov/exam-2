from django.urls import path

from apps.task2.api_endpoints import vacancy

urlpatterns = [
    path("vacancy-list/", vacancy.VacancyListAPIView.as_view(), name="vacancy-list"),
]

