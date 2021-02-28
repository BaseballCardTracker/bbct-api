from django.forms import model_to_dict
from model_bakery import baker
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestBaseballCardViews(APITestCase):
    def test_get_list(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        url = reverse('api:baseballcard-list')
        response = self.client.get(url)
        actual = response.json()
        self.assertQuerysetEqual(cards, actual, transform=model_to_dict)
