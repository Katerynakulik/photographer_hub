from django.db import models
from django.contrib.auth.models import User

class Photoshoot(models.Model):
    # Mentor Note: Basic session info for the waitlist logic
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="sessions/")
    expected_dates = models.CharField(max_length=100, help_text="Example: Late May 2026")
    
    # Pricing logic
    deposit_price = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    photoshoot = models.ForeignKey(Photoshoot, on_delete=models.CASCADE, related_name='bookings')
    # Ми використовуємо рядок 'checkout.Order', щоб уникнути помилки циклічного імпорту
    order = models.ForeignKey('checkout.Order', on_delete=models.CASCADE, related_name='bookings')
    quantity = models.PositiveIntegerField(default=1)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.photoshoot.title} ({self.quantity})"