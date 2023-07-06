import pytest
from django.urls import reverse
from model_bakery import baker


@pytest.fixture
def new_category():
    return baker.make("common.Category")

@pytest.fixture
def new_brand():
    return baker.make("common.Brand")

@pytest.mark.django_db
class TestCommon:
    def test_category_list(self, client):
        url = reverse("category-list")
        response = client.get(url)
        assert response.status_code == 200

    def test_category_products(self, client, new_category):
        url = reverse("category-detail", kwargs={"slug": new_category.slug})
        response = client.get(url)
        assert response.status_code == 200

    def test_brand_lis(self, client):
        url = reverse("brand-list")
        response = client.get(url)
        assert response.status_code == 200

    def test_brand_products(self, client, new_brand):
        url = reverse("brand-detail", kwargs={"slug": new_brand.slug})
        response = client.get(url)
        assert response.status_code == 200
