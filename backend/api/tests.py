from django.test import TestCase, Client
from django.urls import reverse

from api.models import BrandName


class BrandNameTests(TestCase):
    def setUp(self):
        self.url = reverse('brand-names')
        self.client = Client()

    def test_endpoint_exists(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    def test_get_brand_name(self):
        brand_name = BrandName.objects.create(brand_name='Topps')
        response = self.client.get(self.url)
        self.assertEqual(brand_name, response.json())
