from datetime import timedelta

from django.utils.crypto import get_random_string
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SendPhoneCodeSerializer, PhoneVerificationCodeSerializer
from .models import User, VerificationCode
from .tasks import send_verification_code


class SendPhoneVerificationCodeView(APIView):
    @swagger_auto_schema(request_body=SendPhoneCodeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = SendPhoneCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data.get("phone")
        code = get_random_string(allowed_chars="0123456789", length=4)
        verification_code, _ = (
            VerificationCode.objects.update_or_create(phone=phone, defaults={"code": code, "is_verified": False})
        )
        verification_code.expired_at = verification_code.last_sent_time + timedelta(seconds=30)
        verification_code.save(update_fields=["expired_at"])
        # send_verification_code.delay(phone, code)
        return Response({"detail": "Successfully sent email verification code."})


class CheckPhoneVerificationCodeView(CreateAPIView):
    queryset = VerificationCode.objects.all()
    serializer_class = PhoneVerificationCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data.get("phone")
        code = serializer.validated_data.get("code")
        verification_code = self.get_queryset().filter(phone=phone).order_by(
            "-last_sent_time").first()
        if verification_code and verification_code.code != code and verification_code.is_expire:
            raise ValidationError("Verification code invalid.")
        verification_code.is_verified = True
        verification_code.save(update_fields=["is_verified"])

        name = serializer.validated_data.get("name")
        try:
            User.objects.get(phone_number=phone)
        except User.DoesNotExist:
            user = User.objects.create(phone_number=phone, name=name)
            if user:
                from rest_framework.authtoken.models import Token
                token = Token.objects.create(user=user)
                return Response({"Token": token.key})
