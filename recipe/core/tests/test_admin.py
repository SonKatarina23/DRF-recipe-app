from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class AdminTests(TestCase):

    # Run before any other test runs
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='elite@gmail.com',
            password='choke'
        )
        self.regular_user = get_user_model().objects.create_user(
            email='normies@gmail.com',
            password='let me be brutally honest'
        )
        self.client.force_login(self.admin_user)

    def test_users_listed(self):
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)
        self.assertContains(response, self.regular_user.name)
        self.assertContains(response, self.regular_user.email)

    def test_user_change_page(self):
        url = reverse('admin:core_user_change', args=[self.regular_user.id])
        # admin/core/user/1
        response = self.client.get(url)
        # test if page loads successfully
        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        url = reverse('admin:core_user_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
