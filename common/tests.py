from django.test import TestCase
from django.urls import reverse


# Create your tests here.


class CategoryTest(TestCase):
    def test_category_list(self):
        url = reverse('category-list')
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)

    def test_category_detail(self):
        url = reverse('category-detail', kwargs={"slug": "ct1"})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


class BrandTest(TestCase):
    def test_brand_list(self):
        url = reverse('brand-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
