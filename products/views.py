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

@user_passes_test(is_photographer) 
def dashboard(request):
    """ Головна сторінка кабінету з переліком всього контенту """
    products = PhotoProduct.objects.all().order_by('-created_at')
    sessions = Photoshoot.objects.all().order_by('-created_at')
    
    return render(request, 'products/dashboard.html', {
        'products': products,
        'sessions': sessions,
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
            return redirect('photoshoot_detail', pk=new_session.pk)
    else:
        form = PhotoshootForm()
    
    return render(request, 'products/photoshoot_form.html', {
        'form': form, 
        'title': 'Create New Photoshoot'
    })

@user_passes_test(is_photographer)
def edit_session(request, pk):
    """Редагування існуючої фотосесії"""
    session = get_object_or_404(Photoshoot, pk=pk)
    
    if request.method == 'POST':
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
        'edit_mode': True
    })


@user_passes_test(is_photographer)
def add_product(request):
    """Додавання нового фото в магазин"""
    if request.method == 'POST':
        form = PhotoProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New photo added to the shop!")
            return redirect('dashboard')
    else:
        form = PhotoProductForm()
    
    return render(request, 'products/product_form.html', {
        'form': form,
        'title': 'Add New Photo'
    })

@user_passes_test(is_photographer)
def edit_product(request, pk):
    """Редагування фото: показуємо старе, дозволяємо міняти текст"""
    product = get_object_or_404(PhotoProduct, pk=pk)
    if request.method == 'POST':
        form = PhotoProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Updates for '{product.title}' saved!")
            return redirect('dashboard')
    else:
        form = PhotoProductForm(instance=product)
    
    return render(request, 'products/product_form.html', {
        'form': form,
        'product': product, # Передаємо об'єкт для відображення картинки
        'title': 'Edit Photo Details',
        'edit_mode': True
    })

@user_passes_test(is_photographer)
def delete_product(request, pk):
    """Видалення фото"""
    product = get_object_or_404(PhotoProduct, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Photo deleted successfully.")
    return redirect('dashboard')