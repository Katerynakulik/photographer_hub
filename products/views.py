from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import PhotoProduct
from bookings.models import Photoshoot

def is_photographer(user):
    # Mentor Note: Custom permission check for the dashboard access
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.is_photographer

def all_products(request):
    products = PhotoProduct.objects.filter(is_active=True)
    
    # Mentor Note: In the future, fetch this from Order/Purchase model
    owned_photos = [] 
    if request.user.is_authenticated:
        # Placeholder: owned_photos = request.user.userprofile.bought_photos.values_list('id', flat=True)
        pass

    return render(request, 'products/products_list.html', {
        'products': products,
        'owned_photos': owned_photos
    })

@user_passes_test(is_photographer)
def photographer_dashboard(request):
    """ The front-end management hub for the photographer """
    products = PhotoProduct.objects.all()
    sessions = Photoshoot.objects.all()
    
    context = {
        'products': products,
        'sessions': sessions,
    }
    return render(request, 'products/dashboard.html', context)