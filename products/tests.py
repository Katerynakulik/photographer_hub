from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import PhotoProduct
from bookings.models import Photoshoot

class ProductTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Creating users
        self.photographer = User.objects.create_user(username='pro', password='password123')
        self.client_user = User.objects.create_user(username='customer', password='password123')
        
        # Configuring the profile 
        if hasattr(self.photographer, 'userprofile'):
            self.photographer.userprofile.is_photographer = True
            self.photographer.userprofile.save()

        # Creating test data
        self.product = PhotoProduct.objects.create(title="Art Photo", price=15.00, is_active=True)
        self.session = Photoshoot.objects.create(title="Portrait Session", total_price=100.00, is_active=True)

    # US #1:Checking the home page
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # US #7: Checking gallery display
    def test_all_products_view(self):
        response = self.client.get(reverse('all_products'))
        self.assertContains(response, "Art Photo")
        self.assertEqual(response.status_code, 200)

    # US #6: Role-based access (Security)
    def test_non_photographer_cannot_access_dashboard(self):
        self.client.login(username='customer', password='password123')
        response = self.client.get(reverse('dashboard'))
        self.assertNotEqual(response.status_code, 200)