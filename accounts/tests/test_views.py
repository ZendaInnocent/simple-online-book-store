from django.test import TestCase
from django.urls import reverse

from accounts.forms import UserCreationForm


class AccountsAppViewsTest(TestCase):

    def test_user_registration_view(self):
        response = self.client.get(reverse('accounts:signup'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.assertIsInstance(response.context['form'], UserCreationForm)