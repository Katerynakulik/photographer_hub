from django.shortcuts import render, redirect
from django.contrib import messages
from marketing.forms import NewsletterForm
from home.forms import ContactForm
from products.models import PhotoProduct

def home(request):
    featured_products = PhotoProduct.objects.filter(is_active=True).order_by('-created_at')[:6]
    
    context = {
        "newsletter_form": NewsletterForm(),
        "contact_form": ContactForm(),
        "products": featured_products,
    }
    return render(request, "home/home.html", context)

def contact(request):
    if request.method != "POST":
        return redirect("home")
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Thanks! Your message has been sent.")
    else:
        messages.error(request, "Please correct the errors in the form.")
    return redirect("home")

def custom_404(request, exception):
    return render(request, "errors/404.html", status=404)