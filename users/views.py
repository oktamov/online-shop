from django.shortcuts import render
from rest_framework import generics

from users.models import User
from users.serializers import UserRegisterSerializers


# Create your views here.

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializers

