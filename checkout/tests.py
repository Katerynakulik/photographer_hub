from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class CheckoutTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='buyer', password='password123')

    # US #10: Redirect to Stripe when the basket is empty (Security)
    def test_checkout_with_empty_cart_redirects(self):
        self.client.login(username='buyer', password='password123')
        response = self.client.get(reverse('create_checkout_session'))
        self.assertEqual(response.status_code, 302)  # Редирект назад до кошика
