import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def new_user():
    return baker.make("users.User")


@pytest.fixture
def new_product():
    return baker.make("product.Product")


@pytest.fixture
def new_cart():
    return baker.make("cart.Cart")


@pytest.mark.django_db
class TestCart:
    def test_cart_list(self, new_user):
        client = APIClient()
        client.force_authenticate(user=new_user)
        url = reverse("cart-list")
        response = client.get(url)
        assert response.status_code == 200

    def test_cart_create(self, new_user, new_product):
        client = APIClient()
        client.force_authenticate(user=new_user)
        url = reverse("cart-create", kwargs={"product_pk": new_product.pk})
        response = client.post(url)
        assert response.status_code == 201

    def test_cart_detail(self, new_cart, new_user):
        client = APIClient()
        client.force_authenticate(user=new_user)
        url = reverse("cart-detail", kwargs={"pk": new_cart.pk})
        response = client.get(url)
        assert response.status_code == 200

    def test_cart_minus(self, new_cart, new_user, new_product):
        client = APIClient()
        client.force_authenticate(user=new_user)
        url = reverse("cart-quantity-minus", kwargs={"product_pk": new_product.pk})
        response = client.put(url)
        assert response.status_code == 200
