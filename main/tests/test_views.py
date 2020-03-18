from django.test import TestCase
from django.urls import reverse

from main import forms


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

