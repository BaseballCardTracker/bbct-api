from django.forms import model_to_dict
from model_bakery import baker
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from api import models


class TestBaseballCardViews(APITestCase):
    def test_get_list(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        url = reverse('api:baseballcard-list')
        response = self.client.get(url)
        actual = response.json()
        self.assertQuerysetEqual(cards, actual, transform=model_to_dict)

    def test_post_list(self):
        card = baker.prepare('api.BaseballCard', _fill_optional=True)
        url = reverse('api:baseballcard-list')
        data = model_to_dict(card, exclude=('id', ))
        response = self.client.post(url, data=data)
        models.BaseballCard.objects.get(**data)

    def test_get_detail(self):
        card = baker.make('api.BaseballCard')
        url = reverse('api:baseballcard-detail', kwargs={'pk': card.pk})
        response = self.client.get(url)
        expected = model_to_dict(card)
        actual = response.json()
        self.assertEqual(expected, actual)

    def test_put_detail(self):
        card = baker.make('api.BaseballCard')
        url = reverse('api:baseballcard-detail', kwargs={'pk': card.pk})
        edit_card = baker.prepare('api.BaseballCard', _fill_optional=True)
        data = model_to_dict(edit_card, exclude=('id', ))
        response = self.client.put(url, data=data)
        models.BaseballCard.objects.get(**data)

    def test_patch_detail(self):
        card = baker.make('api.BaseballCard')
        url = reverse('api:baseballcard-detail', kwargs={'pk': card.pk})
        edit_card = baker.prepare('api.BaseballCard', _fill_optional=True)
        data = model_to_dict(edit_card, exclude=('id', ))
        response = self.client.patch(url, data=data)
        models.BaseballCard.objects.get(**data)
