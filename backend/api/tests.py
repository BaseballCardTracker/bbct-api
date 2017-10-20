from django.test import TestCase, Client


class EndPointTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_brand_names(self):
        url = '/brand_names/'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
