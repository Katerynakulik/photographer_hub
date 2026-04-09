from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Photoshoot(models.Model):
    """
    Represents a photoshoot theme or event available for booking.
    Contains pricing logic for both deposit and full service cost.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="sessions/")
    expected_dates = models.CharField(
        max_length=100, help_text="Example: Late May 2026")

    # Pricing logic: deposit is paid at checkout, total is for client info
    deposit_price = models.DecimalField(
        max_digits=5, decimal_places=2, default=10.00)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photoshoot_detail', kwargs={'pk': self.pk})


class Booking(models.Model):
    """
    Linking model that represents a confirmed interest/deposit for a photoshoot.
    Connected to a specific order to verify payment.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    photoshoot = models.ForeignKey(
        Photoshoot, on_delete=models.CASCADE, related_name='bookings')
    # Link to Order using string to avoid circular import issues
    order = models.ForeignKey(
        'checkout.Order', on_delete=models.CASCADE, related_name='bookings')
    quantity = models.PositiveIntegerField(default=1)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.photoshoot.title} ({self.quantity})"
