from django.urls import path
from .views import SendVerificationCode, VerifyCode

urlpatterns = [
    path('send_verification_code/', SendVerificationCode.as_view()),
    path('verify_code/', VerifyCode.as_view()),
]
