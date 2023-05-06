from django.urls import path

from apps.task1.api_endpoints.user.CreateUser.views import RegisterAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register')
]
