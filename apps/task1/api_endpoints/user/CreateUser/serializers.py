from rest_framework import serializers

from apps.task1.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        email = validated_data['email']
        user = User.objects.filter(email=email, is_deleted=True).first()
        if user:
            user.set_password(validated_data['password'])
            user.is_deleted = False
            user.save(update_fields=['password', 'is_deleted'])
            return user
        else:
            validated_data['is_deleted'] = False
            return super().create(validated_data)

