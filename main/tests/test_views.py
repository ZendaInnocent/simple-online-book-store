from django.test import TestCase
from django.urls import reverse

from main import forms
from main.models import Product


class TestMainAppViews(TestCase):

    def test_home_page_works(self):
        response = self.client.get(reverse('main:home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')

    
    def test_about_page_works(self):
        response = self.client.get(reverse('main:about'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about.html')


    def test_contact_page_works(self):
        response = self.client.get(reverse('main:contact'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contact.html')
        self.assertIsInstance(response.context['form'], forms.ContactForm)

    
    def test_valid_form_in_contact_page_sends_mail(self):
        response = self.client.post(reverse('main:contact'), {
            'name': 'Test User',
            'message': 'Hi there!',
        }) 

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    
    def test_product_list_view_works(self):
        response = self.client.get(reverse('main:product-list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/product_list.html')

    
    def test_product_detail_view_works(self):
        product = Product.objects.create(name='product-1', price='100.00')
        response = self.client.get(reverse('main:product-detail',
            kwargs={'pk': product.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/product_detail.html')