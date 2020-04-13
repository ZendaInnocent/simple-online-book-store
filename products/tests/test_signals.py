from django.test import TestCase
from products import models
from django.core.files.images import ImageFile
from decimal import Decimal

class TestMainAppSignals(TestCase):
    def test_thumbnails_are_generated_on_save(self):
        product = models.Product(
            name = 'The cathedral and the bazaar',
            price = Decimal('10.00')
        )
        product.save()

        with open('main/fixtures/dark-mode.PNG', 'rb') as f:
            image = models.ProductImage(
                product=product,
                image=ImageFile(f, name='tctb.jpg'),
            )
            image.save()

           
        image.refresh_from_db()

        image.thumbnail.delete(save=False)
        image.image.delete(save=False)