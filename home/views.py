from django.shortcuts import render, redirect
from django.contrib import messages
from marketing.forms import NewsletterForm
from home.forms import ContactForm

def home(request):
    newsletter_form = NewsletterForm()
    contact_form = ContactForm()
    return render(request, "home/home.html", {
        "newsletter_form": newsletter_form,
        "contact_form": contact_form,
    })

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