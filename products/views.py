from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import PhotoProduct
from bookings.models import Photoshoot
from .forms import PhotoProductForm, PhotoshootForm
from checkout.models import Order, PurchasedPhoto
from django.db.models import ProtectedError
from django.db.models import Count


def is_photographer(user):
    """ Security check to ensure only the photographer accesses management views """
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.is_photographer


def all_products(request):
    """
    Displays the shop gallery.
    Fetches IDs of already purchased photos to disable the 'Add to Cart' button.
    """
    products = PhotoProduct.objects.filter(is_active=True)
    purchased_product_ids = []

    if request.user.is_authenticated:
        # Fetch a list of product IDs that the current user has already bought
        purchased_product_ids = list(PurchasedPhoto.objects.filter(
            user=request.user
        ).values_list('product_id', flat=True))

    return render(request, 'products/products_list.html', {
        'products': products,
        # Crucial for the template condition
        'purchased_product_ids': purchased_product_ids
    })


@user_passes_test(is_photographer)
def dashboard(request):
    """ Photographer's main management dashboard """
    products = PhotoProduct.objects.annotate(
        purchase_count=Count('purchasedphoto')).order_by('-created_at')
    sessions = Photoshoot.objects.annotate(
        booking_count=Count('bookings')).order_by('-created_at')
    recent_orders = Order.objects.filter(
        status="paid").order_by('-created_at')[:5]
    return render(request, 'products/dashboard.html', {
        'products': products,
        'sessions': sessions,
        'recent_orders': recent_orders,
    })


def photoshoot_detail(request, pk):
    """ Public detail view for a specific photoshoot session """
    session = get_object_or_404(Photoshoot, pk=pk)
    return render(request, 'products/photoshoot_detail.html', {
        'session': session
    })


@user_passes_test(is_photographer)
def add_session(request):
    """ View for the photographer to create a new photoshoot session """
    if request.method == 'POST':
        form = PhotoshootForm(request.POST, request.FILES)
        if form.is_valid():
            new_session = form.save()
            messages.success(
                request, f"Success! {new_session.title} has been created.")
            return redirect('dashboard')
    else:
        form = PhotoshootForm()

    return render(request, 'products/photoshoot_form.html', {
        'form': form,
        'title': 'Create New Photoshoot'
    })


@user_passes_test(is_photographer)
def edit_session(request, pk):
    """ Photographer view to edit existing session details """
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
    """ Photographer view to add a new digital photo to the shop """
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
    """ Photographer view to update photo details and title """
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
        'product': product,
        'title': 'Edit Photo Details',
        'edit_mode': True
    })


@user_passes_test(is_photographer)
def delete_product(request, pk):
    """
    Safely handles product deletion.
    If purchased, deactivates instead of deleting to preserve records.
    """
    product = get_object_or_404(PhotoProduct, pk=pk)

    if request.method == 'POST':
        try:
            product.delete()
            messages.success(request, "Photo deleted successfully.")
        except ProtectedError:
            # If the photo is already purchased, we just hide it from the shop
            product.is_active = False
            product.save()
            messages.warning(
                request,
                "This photo is already owned by a customer. It has been deactivated "
                "and hidden from the shop instead of deleted.")

    return redirect('dashboard')
