from django.shortcuts import render, redirect
from django.contrib import messages
from marketing.forms import NewsletterForm
from home.forms import ContactForm
from profiles.models import UserProfile
from products.models import PhotoProduct

def home(request):
    """
    Головна сторінка: виводить дані фотографа (адміна) 
    та перші 4 активні продукти для сітки.
    """
    # Знаходимо профілі, де активовано прапорець фотографа
    # Використовуємо select_related для швидкості завантаження імені User
    photographer = UserProfile.objects.filter(is_photographer=True).select_related('user').first()
    
    # Беремо рівно 4 продукти для нашої математично розрахованої сітки
    featured_products = PhotoProduct.objects.filter(is_active=True).order_by('-created_at')[:4]
    
    context = {
        "photographer": photographer,
        "products": featured_products,
        "newsletter_form": NewsletterForm(),
        "contact_form": ContactForm(),
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

def custom_404(request, exception):
    """Кастомна сторінка помилки 404"""
    return render(request, "errors/404.html", status=404)