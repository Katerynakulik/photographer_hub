from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import PhotoProduct


class CartTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='tester', password='password123')
        self.product = PhotoProduct.objects.create(
            title="License", price=10.00)

    # US #9: Add to card
    def test_add_product_to_cart(self):
        self.client.login(username='tester', password='password123')
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
                         'item_type': 'product'})
        session = self.client.session
        self.assertIn(f"p_{self.product.id}", session['cart'])

    # US #9: Duplicate protection (Limit 1 for photos)
    def test_duplicate_photo_not_added(self):
        self.client.login(username='tester', password='password123')
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
                         'item_type': 'product'})
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
                         'item_type': 'product'})
        self.assertEqual(
            self.client.session['cart'][f"p_{self.product.id}"], 1)
