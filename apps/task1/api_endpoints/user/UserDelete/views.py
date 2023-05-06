from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser

from apps.task1.models import User


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
