from rest_framework import serializers

from users.models import User


class UserRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "phone_number"]
