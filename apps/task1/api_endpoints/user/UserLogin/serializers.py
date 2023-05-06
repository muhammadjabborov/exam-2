from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.serializers import ModelSerializer

from apps.task1.models import User


class LoginSerializer(ModelSerializer):
    phone_number = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    first_name = serializers.CharField(max_length=255, read_only=True)
    last_name = serializers.CharField(max_length=255, read_only=True)
    tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone_number", "password", "tokens")

    def validate(self, data):
        phone_number = data.get("phone_number", "")
        password = data.get("password", "")

        user = authenticate(phone_number=phone_number, password=password)

        if not user:
            raise AuthenticationFailed({"message": "The phone number was disabled or doesn't have in database"})

        return {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone_number": user.phone_number,
            "tokens": user.tokens,
        }
