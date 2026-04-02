from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import PhotoProduct
from bookings.models import Photoshoot

def is_photographer(user):
    # Mentor Note: Custom permission check for the dashboard access
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.is_photographer

def all_products(request):
    """ View for the full gallery page """
    products = PhotoProduct.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'products/products_list.html', {'products': products})

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