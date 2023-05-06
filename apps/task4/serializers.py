from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from .models import VerificationCode


class VerificationCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = VerificationCode
        fields = ('phone_number', 'code')
