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

def photoshoot_detail(request, pk):
    """Сторінка детального перегляду конкретної фотосесії"""
    session = get_object_or_404(Photoshoot, pk=pk)
    return render(request, 'products/photoshoot_detail.html', {
        'session': session
    })

@user_passes_test(is_photographer)
def add_session(request):
    """View for the photographer to create a new photoshoot session"""
    if request.method == 'POST':
        form = PhotoshootForm(request.POST, request.FILES)
        if form.is_valid():
            new_session = form.save()
            messages.success(request, f"Success! {new_session.title} has been created.")
            # Redirect straight to the new detail page
            return redirect('photoshoot_detail', pk=new_session.pk)
    else:
        form = PhotoshootForm()
    
    # Mentor Note: Pointing to the new specific form template
    return render(request, 'products/photoshoot_form.html', {
        'form': form, 
        'title': 'Create New Photoshoot'
    })

@user_passes_test(is_photographer)
def edit_session(request, pk):
    """Редагування існуючої фотосесії"""
    session = get_object_or_404(Photoshoot, pk=pk)
    
    if request.method == 'POST':
        # instance=session каже Django оновити існуючий запис, а не створювати новий
        form = PhotoshootForm(request.POST, request.FILES, instance=session)
        if form.is_valid():
            form.save()
            messages.success(request, f"Changes to '{session.title}' saved!")
            return redirect('dashboard')
    else:
        form = PhotoshootForm(instance=session)
    
    return render(request, 'products/photoshoot_form.html', {
        'form': form,
        'title': f'Edit: {session.title}',
        'edit_mode': True # Допоможе нам змінити текст на кнопці
    })