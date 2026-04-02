from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages # <--- Не забудь додати цей імпорт
from django.urls import reverse
from .models import PhotoProduct
from bookings.models import Photoshoot
from .forms import PhotoProductForm, PhotoshootForm

def is_photographer(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.is_photographer

def all_products(request):
    products = PhotoProduct.objects.filter(is_active=True)
    owned_photos = [] 
    # В майбутньому тут буде логіка перевірки куплених фото
    return render(request, 'products/products_list.html', {
        'products': products,
        'owned_photos': owned_photos
    })

@user_passes_test(is_photographer) # <--- Додав захист для основної сторінки дашборду
def dashboard(request):
    """ Головна сторінка кабінету з переліком всього контенту """
    products = PhotoProduct.objects.all().order_by('-created_at')
    sessions = Photoshoot.objects.all().order_by('-created_at')
    
    return render(request, 'products/dashboard.html', {
        'products': products,
        'sessions': sessions,
    })

@user_passes_test(is_photographer)
def add_product(request):
    """ Додавання нового фото через фронтенд """
    if request.method == 'POST':
        form = PhotoProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Success! New photo added to the gallery.")
            return redirect('dashboard')
    else:
        form = PhotoProductForm()
    
    return render(request, 'products/manage_item.html', {
        'form': form, 
        'title': 'Add New Photo'
    })

@user_passes_test(is_photographer)
def add_session(request):
    """ Додавання нової фотосесії через фронтенд """
    if request.method == 'POST':
        form = PhotoshootForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Success! New photoshoot is now on the waitlist.")
            return redirect('dashboard')
    else:
        form = PhotoshootForm()
    
    return render(request, 'products/manage_item.html', {
        'form': form, 
        'title': 'Add New Photoshoot'
    })