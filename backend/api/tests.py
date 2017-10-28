import json

from django.test import TestCase
from django.urls import reverse

from api.models import BrandName, PlayerName, TeamName, Position


class BbctTests:
    def test_get(self):
        for field in self.fields:
            self.model_class.objects.create(**field)
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        result = json.loads(response.json())

        for expected, actual in zip(self.fields, result):
            self.assertEqual(expected, actual['fields'])

    def test_post(self):
        fields_json = json.dumps(self.fields[0])
        response = self.client.post(self.url, data=fields_json, content_type='application/json')
        self.assertEqual(200, response.status_code)
        data = json.loads(response.json())
        self.assertEqual(self.fields[0], data[0]['fields'])


class BrandNameTests(TestCase, BbctTests):
    def setUp(self):
        self.model_class = BrandName
        self.field_name = 'brand_name'
        self.fields = [{self.field_name: 'Topps'},
                       {self.field_name: 'Upper Deck'}]
        self.url = reverse('brand-names')


class PlayerNameTests(TestCase, BbctTests):
    def setUp(self):
        self.model_class = PlayerName
        self.field_name = 'player_name'
        self.fields = [{self.field_name: 'Alex Fernandez'},
                       {self.field_name: 'Dave Hollins'}]
        self.url = reverse('player-names')


class TeamNameTests(TestCase, BbctTests):
    def setUp(self):
        self.model_class = TeamName
        self.field_name = 'team_name'
        self.fields = [{self.field_name: 'White Sox'},
                       {self.field_name: 'Phillies'}]
        self.url = reverse('team-names')


class PositionTests(TestCase, BbctTests):
    def setUp(self):
        self.model_class = Position
        self.field_name = 'position'
        self.fields = [{self.field_name: 'Pitcher'},
                       {self.field_name: 'Third Base'}]
        self.url = reverse('positions')
