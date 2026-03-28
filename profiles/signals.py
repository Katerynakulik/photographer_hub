from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from .models import UserProfile
from marketing.models import NewsletterSubscriber

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Створює профіль користувача автоматично при створенні User"""
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

@receiver(user_signed_up)
def handle_newsletter_subscription(request, user, **kwargs):
    """Додає в розсилку тільки якщо стоїть галочка при реєстрації"""
    # Перевіряємо дані з POST запиту форми реєстрації
    subscribe = request.POST.get('subscribe_newsletter')
    
    if subscribe:
        NewsletterSubscriber.objects.get_or_create(email=user.email)