from django.urls import path

from users.views import UserRegisterView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name='user-register')
]
