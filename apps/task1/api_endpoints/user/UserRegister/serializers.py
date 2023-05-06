from django.contrib.auth.hashers import make_password
from django.db.transaction import atomic
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.task1.models import User


class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=68, write_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone_number", "password", "password2")

    def validate(self, data):
        password = data.get("password")
        password2 = data.get("password2")

        if password != password2:
            raise serializers.ValidationError({"message": "Password didn't match"})

        return data

    @atomic
    def create(self, validated_data):
        validated_data.pop('password2')
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create_user(**validated_data)
        return user
