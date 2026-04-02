from django.shortcuts import render, redirect
from django.contrib import messages
from marketing.forms import NewsletterForm
from home.forms import ContactForm
from profiles.models import UserProfile
from products.models import PhotoProduct
from bookings.models import Photoshoot

def home(request):
    photographer = UserProfile.objects.filter(is_photographer=True).select_related('user').first()
    featured_products = PhotoProduct.objects.filter(is_active=True).order_by('-created_at')[:4]
    
    # Mentor Note: Fetch active photoshoots for the landing page
    sessions = Photoshoot.objects.filter(is_active=True).order_by('created_at')

    context = {
        "photographer": photographer,
        "products": featured_products,
        "sessions": sessions,
        "newsletter_form": NewsletterForm(),
    }
    return render(request, "home/home.html", context)

def contact(request):
    """Обробка форми зворотного зв'язку"""
    if request.method != "POST":
        return redirect("home")
    
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Your message has been sent successfully!")
    else:
        messages.error(request, "There was an error with your submission. Please check the form.")
    
    return redirect("home")

def handle_404(request, exception):
    return render(request, "404.html", status=404)

def handle_500(request):
    return render(request, "500.html", status=500)