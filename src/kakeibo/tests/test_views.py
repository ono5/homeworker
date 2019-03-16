from django.urls import resolve
from django.test import TestCase
from kakeibo.views import kakeibo_page


class KakeiboTest(TestCase):
    def test_url_resolves_to_kakeibo_page_view(self):
        """
        GIVEN /kakeibo/URL
        WHEN access to localhost:8000/kakeibo/
        THEN return kakeibo_page function
        """
        found = resolve('/kakeibo/')
        assert found.func == kakeibo_page

    def test_return_template(self):
        """
        GIVEN /kakeibo/URL
        WHEN access to localhost:8000/kakeibo/
        THEN return kakeibo.html
        """
        response = self.client.get('/kakeibo/')
        self.assertTemplateUsed(response, 'kakeibo/kakeibo.html')

