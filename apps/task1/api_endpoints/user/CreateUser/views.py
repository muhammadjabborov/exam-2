from rest_framework.generics import CreateAPIView

from apps.task1.api_endpoints.user.CreateUser.serializers import UserRegistrationSerializer
from apps.task1.models import User


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
