from django.urls import resolve
from django.test import TestCase, Client
from kakeibo.views import kakeibo_page
from kakeibo.models import Payment

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


class KakeiboListTest(TestCase):
    def test_get_list(self):
        """
        GIVEN /kakeibo/list/
        WHEN access to localhost:8000/kakeibo/list/
        THEN return Payment list
        """
        payment_list = Payment.objects.all()
        print(payment_list)
