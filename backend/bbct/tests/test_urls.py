from django.test import TestCase
from django.urls import reverse


class TestSocialUrls(TestCase):
    def test_social_login_url(self):
        url = reverse('social:begin', kwargs={'backend': 'google-oauth2'})
        expected = '/social/login/google-oauth2/'
        self.assertEqual(expected, url)

    def test_social_complete_url(self):
        url = reverse('social:complete', kwargs={'backend': 'google-oauth2'})
        expected = '/social/complete/google-oauth2/'
        self.assertEqual(expected, url)
