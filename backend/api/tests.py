import json

from django.test import TestCase
from django.urls import reverse

from api.models import BrandName, PlayerName, TeamName, Position


class BbctTests:
    def test_endpoint_exists(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    def test_get(self):
        self.model_class.objects.create(**self.fields)
        response = self.client.get(self.url)
        result = json.loads(response.json())
        self.assertEqual(self.fields, result[0]['fields'])


class BrandNameTests(TestCase, BbctTests):
    def setUp(self):
        self.model_class = BrandName
        self.fields = {'brand_name': 'Topps'}
        self.url = reverse('brand-names')


class PlayerNameTests(TestCase, BbctTests):
    def setUp(self):
        self.model_class = PlayerName
        self.fields = {'player_name': 'Alex Fernandez'}
        self.url = reverse('player-names')


class TeamNameTests(TestCase, BbctTests):
    def setUp(self):
        self.model_class = TeamName
        self.fields = {'team_name': 'White Sox'}
        self.url = reverse('team-names')


class PositionTests(TestCase, BbctTests):
    def setUp(self):
        self.model_class = Position
        self.fields = {'position': 'Pitcher'}
        self.url = reverse('positions')
