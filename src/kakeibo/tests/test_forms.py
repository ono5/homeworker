from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

import pytest

from kakeibo.forms import KakeiboInputForm
from kakeibo.models import Category, Payment


class KakeiboFormTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            password='test123',
            email='admin@co.jp'
        )

    def test_form_input_has_placeholder_and_css_classes(self):
        form = KakeiboInputForm()
        assert 'placeholder="Enter a credit for item"' in form.as_p()
        assert 'class="form-control input-lg"' in form.as_p()

    def test_form_input_save(self):
        Category.objects.create(category_item='FOOD')
        category_ = Category.objects.get(id=1)
        form = KakeiboInputForm(data={
            'category': category_.id,
            'item': 'Mac',
            'credit': 1000,

        })
        # Form can not save without validation
        if form.is_valid():
            print('#########', self.admin_user)
            form.save(self.admin_user)
        else:
            print('#########ERROR#########')

        item = Payment.objects.all()
        assert item.count() == 1
