from django.test import TestCase

from accounts.models import CustomUser


class AccountsModelsTests(TestCase):

    def setUp(self):
        self.superuser = CustomUser.objects.create_superuser(
            email='superuser@admin.com',
            name='super user'
        )
        self.user = CustomUser.objects.create_user(
            email='test@user.com',
            name = 'test user',
        )
    
    def test_raise_message_when_create_user_with_invalid_email(self):
        self.assertRaisesMessage(ValueError, 'Users must have an email address', CustomUser.objects.create_user, email='', name='odsif')

    def test_custom_user_string_representation(self):
        user = self.user
        self.assertEqual(str(user), self.user.email)

    def test_staff_property(self):
        superuser = self.superuser
        self.assertTrue(superuser.is_staff)
