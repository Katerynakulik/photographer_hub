from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
# Змінено з Mailchimp на MailChimp (Велика 'C')
from mailchimp3 import MailChimp


def subscribe_email(email):
    """ Helper function to add email to Mailchimp Audience """
    # Тут також міняємо на MailChimp
    client = MailChimp(mc_api=settings.MAILCHIMP_API_KEY,
                       mc_user='photographer_hub')

    try:
        client.lists.members.create(settings.MAILCHIMP_EMAIL_LIST_ID, {
            'email_address': email,
            'status': 'subscribed',
        })
        return True
    except Exception:
        return False


def newsletter_subscribe(request):
    """ View for the home page newsletter form """
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            success = subscribe_email(email)
            if success:
                messages.success(
                    request, "Success! You are now part of the journey.")
            else:
                # Often fails if email is already in the list
                messages.info(
                    request, "Check your inbox or you might be already subscribed.")

    return redirect("home")
