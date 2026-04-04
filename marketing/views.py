import json
import requests
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from mailchimp3 import Mailchimp

def subscribe_email(email):
    """ Helper function to add email to Mailchimp Audience """
    client = Mailchimp(mc_api=settings.MAILCHIMP_API_KEY, mc_user='photographer_hub')
    
    try:
        client.lists.members.create(settings.MAILCHIMP_EMAIL_LIST_ID, {
            'email_address': email,
            'status': 'subscribed',
        })
        return True
    except Exception as e:
        return False

def newsletter_subscribe(request):
    """ View for the home page newsletter form """
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            success = subscribe_email(email)
            if success:
                messages.success(request, "Success! You are now part of the journey.")
            else:
                messages.info(request, "You are already subscribed or there was an error.")
    
    return redirect("home")