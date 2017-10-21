from django.test import TestCase, Client
from django.urls import reverse


class BrandNameTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_endpoint_exists(self):
        url = reverse('brand-names')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
