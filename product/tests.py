import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def new_product():
    return baker.make("product.Product")


@pytest.fixture
def new_user():
    return baker.make("users.User")


@pytest.mark.django_db
class TestProduct:
    def test_product(self, client):
        url = reverse("product-list")
        response = client.get(url)
        assert response.status_code == 200

    def test_product_detail(self, client, new_product):
        url = reverse("product-detail", kwargs={"slug": new_product.slug})
        response = client.get(url)
        assert response.status_code == 200

    def test_product_review(self, client, new_product):
        data = {
            "product": new_product.id,
            "comment": "string",
            "ratings": "1"
        }
        url = reverse("product-reviews")
        response = client.post(url, data=data)
        assert response.status_code == 201

    def test_product_liked(self, new_user, new_product):
        client = APIClient()
        client.force_authenticate(user=new_user)
        url = reverse("product-like-unlike", kwargs={"slug": new_product.slug})
        response = client.post(url)
        assert response.status_code == 200

    def test_product_liked_list(self, new_user):
        client = APIClient()
        client.force_authenticate(user=new_user)
        url = reverse("product-liked-list")
        response = client.get(url)
        assert response.status_code == 200
