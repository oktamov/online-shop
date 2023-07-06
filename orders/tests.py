import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def new_user():
    return baker.make("users.User")


@pytest.mark.django_db
class TestOrders:
    def test_orders_list(self, new_user):
        client = APIClient()
        client.force_authenticate(user=new_user)
        url = reverse('orders-list')
        response = client.get(url)
        assert response.status_code == 200

    def test_orders_create(self, new_user):
        data = {
            "user": new_user.id,
            "name": "string",
            "phone": "string",
            "region": "string",
            "city": "string",
            "village": "string",
            "address": "string",
            "job_address": "string",
            "addition": "string",
            "promo_kod": "string",
            "pyment": "Naqd pul"
        }
        client = APIClient()
        client.force_authenticate(user=new_user)
        url = reverse('orders-create')
        response = client.post(url, data=data)
        assert response.status_code == 200
