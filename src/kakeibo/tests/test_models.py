from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.utils.html import escape

import pytest

from kakeibo.models import Category, Payment


class CategoryAndPaymentTest(TestCase):
    def test_cannot_save_payment_without_selecting_category(self):
        """
        GIVEN without selecting category
        WHEN save payment
        THEN raise IntegrityError Error

        Foreignkey -> IntegrityError
        Not Foreignkey -> ValidationError
        """
        payment = Payment(credit=2000, item="humbarger")
        with self.assertRaises(IntegrityError):
            payment.save()
            payment.full_clean()

    def test_cannot_save_payment_without_selecting_credit(self):
        category_ = Category.objects.create(category_item='food')
        payment = Payment(category=category_, item='humbarger')
        with self.assertRaises(ValidationError):
            payment.save()
            payment.full_clean()

    def test_cannot_save_payment_without_selecting_credit(self):
        category_ = Category.objects.create(category_item='food')
        payment = Payment(category=category_, item='humbarger')
        with self.assertRaises(ValidationError):
            payment.save()
            payment.full_clean()

    def test_cannot_save_payment_without_selecting_item(self):
        category_ = Category.objects.create(category_item='food')
        payment = Payment(category=category_, credit=1000)
        with self.assertRaises(ValidationError):
            payment.save()
            payment.full_clean()