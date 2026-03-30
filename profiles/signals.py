from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from .models import UserProfile
from marketing.models import NewsletterSubscriber

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Створює профіль автоматично"""
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

@receiver(user_signed_up)
def handle_newsletter_subscription(request, user, **kwargs):
    """Обробляє підписку на розсилку при реєстрації"""
    # Ми беремо дані прямо з нашої нової форми
    subscribe = request.POST.get('subscribe_newsletter')
    
    if subscribe:
        # Додаємо імейл в список маркетингу
        NewsletterSubscriber.objects.get_or_create(email=user.email)