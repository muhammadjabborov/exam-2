from django.urls import path

from apps.task1.api_endpoints.user.UserDelete.views import UserDeleteAPIView
from apps.task1.api_endpoints.user.UserLogin.views import LoginAPIView
from apps.task1.api_endpoints.user.UserRegister.views import RegisterAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="user-register"),
    path("login/", LoginAPIView.as_view(), name="user-login"),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete')
]
