from django.test import TestCase, Client


class BrandNameTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_endpoint_exists(self):
        url = '/api/brand_names/'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
