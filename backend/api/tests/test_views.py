from django.contrib.auth import get_user_model
from django.forms import model_to_dict
from model_bakery import baker
from rest_framework import status
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


class TestCollectionViews(APITestCase):
    def setUp(self):
        self.user = baker.make(get_user_model())
        self.client.force_login(self.user)

    def test_get_list(self):
        collections = baker.make('api.Collection', user=self.user, _quantity=2)
        other_user = baker.make(get_user_model())
        other_collection = baker.make('api.Collection', user=other_user)
        url = reverse('api:collection-list')
        response = self.client.get(url)
        actual = response.json()
        self.assertQuerysetEqual(collections, actual, transform=model_to_dict)

    def test_post_list(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        url = reverse('api:collection-list')
        data = {
            'user': self.user.pk,
            'cards': [card.pk for card in cards],
        }
        response = self.client.post(url, data=data)
        collection = models.Collection.objects.get(user=self.user.pk)
        self.assertQuerysetEqual(
            collection.cards.order_by('pk'),
            cards,
            transform=lambda x: x
        )

    def test_get_detail(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        collection = baker.make('api.Collection', user=self.user, cards=cards)
        url = reverse('api:collection-detail', kwargs={'pk': collection.pk})
        response = self.client.get(url)
        expected = {
            'id': collection.pk,
            'user': self.user.pk,
            'cards': [card.pk for card in cards]
        }
        actual = response.json()
        self.assertEqual(expected, actual)

    def test_get_detail_not_owned(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        other_user = baker.make(get_user_model())
        collection = baker.make('api.Collection', user=other_user, cards=cards)
        url = reverse('api:collection-detail', kwargs={'pk': collection.pk})
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_put_detail(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        collection = baker.make('api.Collection', user=self.user, cards=cards)
        url = reverse('api:collection-detail', kwargs={'pk': collection.pk})
        edit_user = baker.make(get_user_model())
        edit_cards = baker.make('api.BaseballCard', _quantity=3)
        data = {
            'user': edit_user.pk,
            'cards': [card.pk for card in edit_cards],
        }
        response = self.client.put(url, data=data)
        collection = models.Collection.objects.get(user=edit_user.pk)
        self.assertQuerysetEqual(
            collection.cards.order_by('pk'),
            edit_cards,
            transform=lambda x: x
        )

    def test_put_detail_not_owned(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        other_user = baker.make(get_user_model())
        collection = baker.make('api.Collection', user=other_user, cards=cards)
        url = reverse('api:collection-detail', kwargs={'pk': collection.pk})
        edit_user = baker.make(get_user_model())
        edit_cards = baker.make('api.BaseballCard', _quantity=3)
        data = {
            'user': edit_user.pk,
            'cards': [card.pk for card in edit_cards],
        }
        response = self.client.put(url, data=data)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_patch_detail(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        collection = baker.make('api.Collection', user=self.user, cards=cards)
        url = reverse('api:collection-detail', kwargs={'pk': collection.pk})
        edit_user = baker.make(get_user_model())
        edit_cards = baker.make('api.BaseballCard', _quantity=3)
        data = {
            'user': edit_user.pk,
            'cards': [card.pk for card in edit_cards],
        }
        response = self.client.patch(url, data=data)
        collection = models.Collection.objects.get(user=edit_user.pk)
        self.assertQuerysetEqual(
            collection.cards.order_by('pk'),
            edit_cards,
            transform=lambda x: x
        )

    def test_patch_detail_not_owned(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        other_user = baker.make(get_user_model())
        collection = baker.make('api.Collection', user=other_user, cards=cards)
        url = reverse('api:collection-detail', kwargs={'pk': collection.pk})
        edit_user = baker.make(get_user_model())
        edit_cards = baker.make('api.BaseballCard', _quantity=3)
        data = {
            'user': edit_user.pk,
            'cards': [card.pk for card in edit_cards],
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)


class TestCollectionAnonymous(APITestCase):
    def setUp(self):
        self.user = baker.make(get_user_model())

    def test_get_list_anonymous(self):
        collections = baker.make('api.Collection', user=self.user, _quantity=3)
        url = reverse('api:collection-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_post_list_anonymous(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        url = reverse('api:collection-list')
        data = {
            'user': self.user.pk,
            'cards': [card.pk for card in cards],
        }
        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_get_detail_anonymous(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        collection = baker.make('api.Collection', user=self.user, cards=cards)
        url = reverse('api:collection-detail', kwargs={'pk': collection.pk})
        response = self.client.get(url)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_put_detail_anonymous(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        collection = baker.make('api.Collection', user=self.user, cards=cards)
        url = reverse('api:collection-detail', kwargs={'pk': collection.pk})
        edit_user = baker.make(get_user_model())
        edit_cards = baker.make('api.BaseballCard', _quantity=3)
        data = {
            'user': edit_user.pk,
            'cards': [card.pk for card in edit_cards],
        }
        response = self.client.put(url, data=data)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_patch_detail_anonymous(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        collection = baker.make('api.Collection', user=self.user, cards=cards)
        url = reverse('api:collection-detail', kwargs={'pk': collection.pk})
        edit_user = baker.make(get_user_model())
        edit_cards = baker.make('api.BaseballCard', _quantity=3)
        data = {
            'user': edit_user.pk,
            'cards': [card.pk for card in edit_cards],
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)


class TestCollectionSuperuser(APITestCase):
    def setUp(self):
        self.user = baker.make(get_user_model())
        superuser = baker.make(get_user_model(), is_superuser=True)
        self.client.force_login(superuser)

    def test_get_list_superuser(self):
        collections = baker.make('api.Collection', user=self.user, _quantity=2)
        other_user = baker.make(get_user_model())
        other_collection = baker.make('api.Collection', user=other_user)
        url = reverse('api:collection-list')
        response = self.client.get(url)
        expected = models.Collection.objects.order_by('pk')
        actual = response.json()
        self.assertQuerysetEqual(expected, actual, transform=model_to_dict)

    def test_post_list_superuser(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        url = reverse('api:collection-list')
        data = {
            'user': self.user.pk,
            'cards': [card.pk for card in cards],
        }
        response = self.client.post(url, data=data)
        collection = models.Collection.objects.get(user=self.user.pk)
        self.assertQuerysetEqual(
            collection.cards.order_by('pk'),
            cards,
            transform=lambda x: x
        )

    def test_get_detail_superuser(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        collection = baker.make('api.Collection', user=self.user, cards=cards)
        url = reverse('api:collection-detail', kwargs={'pk': collection.pk})
        response = self.client.get(url)
        expected = {
            'id': collection.pk,
            'user': self.user.pk,
            'cards': [card.pk for card in cards]
        }
        actual = response.json()
        self.assertEqual(expected, actual)

    def test_put_detail_superuser(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        collection = baker.make('api.Collection', user=self.user, cards=cards)
        url = reverse('api:collection-detail', kwargs={'pk': collection.pk})
        edit_user = baker.make(get_user_model())
        edit_cards = baker.make('api.BaseballCard', _quantity=3)
        data = {
            'user': edit_user.pk,
            'cards': [card.pk for card in edit_cards],
        }
        response = self.client.put(url, data=data)
        collection = models.Collection.objects.get(user=edit_user.pk)
        self.assertQuerysetEqual(
            collection.cards.order_by('pk'),
            edit_cards,
            transform=lambda x: x
        )

    def test_patch_detail_superuser(self):
        cards = baker.make('api.BaseballCard', _quantity=3)
        collection = baker.make('api.Collection', user=self.user, cards=cards)
        url = reverse('api:collection-detail', kwargs={'pk': collection.pk})
        edit_user = baker.make(get_user_model())
        edit_cards = baker.make('api.BaseballCard', _quantity=3)
        data = {
            'user': edit_user.pk,
            'cards': [card.pk for card in edit_cards],
        }
        response = self.client.patch(url, data=data)
        collection = models.Collection.objects.get(user=edit_user.pk)
        self.assertQuerysetEqual(
            collection.cards.order_by('pk'),
            edit_cards,
            transform=lambda x: x
        )
