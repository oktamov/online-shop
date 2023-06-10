from django.urls import path

from users.views import SendPhoneVerificationCodeView, CheckPhoneVerificationCodeView

urlpatterns = [
    path('send-code', SendPhoneVerificationCodeView.as_view()),
    path('check-code', CheckPhoneVerificationCodeView.as_view()),
]
