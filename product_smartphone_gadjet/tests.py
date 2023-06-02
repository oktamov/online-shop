from django.test import TestCase
from django.urls import reverse


# Create your tests here.


class SmartphoneAndGadjetTest(TestCase):
    def test_phone_list(self):
        url = reverse('phone-list')
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
