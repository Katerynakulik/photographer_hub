from django.db import models
from django.contrib.auth.models import User
from products.models import PhotoProduct

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.CharField(max_length=20, default="pending") # pending, paid, failed
    stripe_session_id = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class PurchasedPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(PhotoProduct, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)