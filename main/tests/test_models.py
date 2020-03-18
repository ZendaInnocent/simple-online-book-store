from django.test import TestCase
from decimal import Decimal

from main import models


class TestModel(TestCase):

    def test_product_string_representation(self):
        product = models.Product.objects.create(
            name = 'the first product',
            price = Decimal('2.00'),
        )

        self.assertEqual(str(product), product.name)


    def test_product_manager_works(self):
        models.Product.objects.create(
            name = 'the first product',
            price = Decimal('2.00'),
            active = False,
        )
        models.Product.objects.create(
            name = 'the second product',
            price = Decimal('21.00')
        )
        models.Product.objects.create(
            name = 'the third product',
            price = Decimal('12.00'),
            active = True,
        )

        self.assertEqual(len(models.Product.objects.active()), 2)