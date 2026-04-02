from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    is_photographer = models.BooleanField(default=False)
    profile_image = CloudinaryField('image', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    tagline = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        # Повертаємо ім'я користувача, якщо воно вказане, інакше - username
        return self.user.get_full_name() or self.user.username