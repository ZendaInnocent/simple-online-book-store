from django.test import TestCase
from django.urls import reverse

from products.models import Product


class TestProductsAppViews(TestCase):
    
    def test_product_list_view_works(self):
        response = self.client.get(reverse('products:product-list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_product_list_show_no_product_yet(self):
        """Test if it shows the message when no product listed in db"""
        response = self.client.get(reverse('products:product-list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No products yet.')

    
    def test_product_detail_view_works(self):
        product = Product.objects.create(name='product-1', price='100.00')
        response = self.client.get(reverse('products:product-detail',
            kwargs={'pk': product.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')