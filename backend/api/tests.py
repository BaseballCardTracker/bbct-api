import json

from django.test import TestCase, Client
from django.urls import reverse

from api.models import BrandName, PlayerName


class BbctTests:
    def test_endpoint_exists(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)


class BrandNameTests(TestCase, BbctTests):
    def setUp(self):
        self.model_class = BrandName
        self.fields = {'brand_name': 'Topps'}
        self.url = reverse('brand-names')
        self.client = Client()

    def test_get_brand_names(self):
        self.model_class.objects.create(**self.fields)
        response = self.client.get(self.url)
        result = json.loads(response.json())
        self.assertEqual(self.fields, result[0]['fields'])


class PlayerNameTests(TestCase, BbctTests):
    def setUp(self):
        self.model_class = PlayerName
        self.fields = {'player_name': 'Alex Fernandez'}
        self.url = reverse('player-names')
        self.client = Client()

    def test_get_player_names(self):
        self.model_class.objects.create(**self.fields)
        response = self.client.get(self.url)
        result = json.loads(response.json())
        self.assertEqual(self.fields, result[0]['fields'])
