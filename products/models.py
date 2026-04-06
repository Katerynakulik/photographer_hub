from django.db import models
from django.utils.text import slugify

class PhotoProduct(models.Model):
    """
    Catalog of digital photography available for purchase.
    Uses slugs for SEO-friendly URLs.
    """
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    preview_image = models.ImageField(upload_to="products/previews/")
    digital_file = models.FileField(upload_to="products/files/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generate slug automatically from title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title