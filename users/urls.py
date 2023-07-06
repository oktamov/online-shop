from django.urls import path

from users.views import SendPhoneVerificationCodeView, CheckPhoneVerificationCodeView

urlpatterns = [
    path('send-code', SendPhoneVerificationCodeView.as_view(), name='send-code'),
    path('check-code/login', CheckPhoneVerificationCodeView.as_view(), name='check-code'),
]
