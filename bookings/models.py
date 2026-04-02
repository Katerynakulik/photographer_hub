from django.db import models

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