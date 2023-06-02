from django.test import TestCase
from django.urls import reverse

from users.models import User


# Create your tests here.


class UserTest(TestCase):
    def setUp(self):
        User.objects.create(phone="+998913973081", full_name="mr ali")
        self.user_data = {
            "full_name": "mr ali",
            "phone": "+998913973081"

        }

    def test_register_user(self):
        url = reverse("user-register")
        response = self.client.post(url, self.user_data)

        self.assertEquals(response.status_code, 201)
