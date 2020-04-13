from django.test import TestCase
from django.urls import reverse, resolve

from products import views


class TestProductsAppUrls(TestCase):

    def test_product_list_url_resolves(self):
        product_list_url = reverse('products:product-list')
        self.assertEqual(resolve(product_list_url).func.view_class, views.ProductListView)

    
    def test_product_detail_url_resolves(self):
        product_detail_url = reverse('products:product-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(product_detail_url).func.view_class, views.ProductDetailView)