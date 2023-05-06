from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import VerificationCode
from .serializers import VerificationCodeSerializer
import random


class SendVerificationCode(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        if VerificationCode.objects.filter(phone_number=phone_number,
                                           created_at__gt=timezone.now() - timezone.timedelta(minutes=2)).exists():
            return Response({'detail': 'Verification code has already been sent recently.'},
                            status=status.HTTP_400_BAD_REQUEST)
        code = random.randint(1, 1234564)
        print(code)
        # TODO code is here
        serializer = VerificationCodeSerializer(data={'phone_number': phone_number, 'code': code})
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Verification code sent successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyCode(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')
        if VerificationCode.objects.filter(phone_number=phone_number, code=code,
                                           created_at__gt=timezone.now() - timezone.timedelta(minutes=2)).exists():
            return Response({'detail': 'Verification code verified successfully.'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid verification code.'}, status=status.HTTP_400_BAD_REQUEST)
