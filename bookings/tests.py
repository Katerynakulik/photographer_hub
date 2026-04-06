from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from bookings.models import Photoshoot
from profiles.models import UserProfile # Переконайтеся, що шлях до моделі правильний

class BookingTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='photograph', 
            password='2HL@UCvgvVzD8d3'
        )
        
        self.profile, created = UserProfile.objects.get_or_create(user=self.user)
        self.profile.is_photographer = True
        self.profile.save()
        
        self.session = Photoshoot.objects.create(
            title="Winter Shoot", 
            total_price=50.00,
            is_active=True
        )

    def test_delete_session_by_photographer(self):
        """ US #15: Verify photographer can delete a session """
        self.client.login(username='photograph', password='2HL@UCvgvVzD8d3')
        response = self.client.post(reverse('delete_session', args=[self.session.id]))
        
        self.assertEqual(response.status_code, 302) # Redirect to dashboard
        self.assertEqual(Photoshoot.objects.count(), 0)