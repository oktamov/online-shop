from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', 'name')


class SendPhoneCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)


class PhoneVerificationCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    code = serializers.CharField(min_length=4, max_length=4)
    name = serializers.CharField(max_length=255, allow_blank=True)
