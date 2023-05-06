from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import LoginSerializer


class LoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer

