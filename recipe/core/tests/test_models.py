from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@gmail.com'
        password = '420-69-322'
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        # password is hashed so you cannot directly compare them
        self.assertTrue(user.check_password(password))

    def test_email_normalize(self):
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email=email, password='SDFSKJFS')
        self.assertEqual(user.email, email.lower())

    def test_email_invalid(self):
        with self.assertRaises(ValueError):
            # If anything inside this indent does not raise ValueError, test will fail
            get_user_model().objects.create_user(email=None, password='DJFNSKJDFZN')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            email='chad@getlaidin2020.com', password="SDFJKSDF")
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
