from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from .views import subscribe_email

@receiver(user_signed_up)
def subscribe_on_signup(sender, request, user, **kwargs):
    # Check if the user ticked the 'subscribe' checkbox in CustomSignupForm
    # Assuming the field name in your form is 'subscribe_newsletter'
    if request.POST.get('subscribe_newsletter'):
        subscribe_email(user.email)