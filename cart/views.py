from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import PhotoProduct
from bookings.models import Photoshoot

@login_required
def view_cart(request):
    return render(request, 'cart/cart.html')

@login_required
def add_to_cart(request, item_id):
    """
    Handles adding items to the session-based cart.
    Logic differs between digital products (limit 1) and session deposits (incremental).
    """
    cart = request.session.get('cart', {})
    item_type = request.POST.get('item_type', 'product')
    
    if item_type == 'session':
        item = get_object_or_404(Photoshoot, pk=item_id)
        item_key = f"s_{item_id}"
        display_name = f"Deposit: {item.title}"
        
        # For sessions: increase quantity if already in cart
        if item_key in cart:
            cart[item_key] += 1
            messages.success(request, f"Another spot added for {item.title}.")
        else:
            cart[item_key] = 1
            messages.success(request, f"Success! {display_name} added to your cart.")
    
    else:
        # For digital photos: limit to exactly 1 license per order
        item = get_object_or_404(PhotoProduct, pk=item_id)
        item_key = f"p_{item_id}"
        display_name = item.title

        if item_key not in cart:
            cart[item_key] = 1
            messages.success(request, f"Digital license for {display_name} added to your cart.")
        else:
            messages.info(request, "This license is already in your cart (limit 1).")
    
    request.session['cart'] = cart
    return redirect(request.POST.get('redirect_url', reverse('home')))


def remove_from_cart(request, item_key):
    cart = request.session.get('cart', {})
    if item_key in cart:
        del cart[item_key]
        messages.success(request, "Item removed from your cart.")
    
    request.session['cart'] = cart
    return redirect('view_cart')

def adjust_cart(request, item_key):
    """Adjust quantity for sessions or remove items"""
    cart = request.session.get('cart', {})
    action = request.POST.get('action')

    if item_key in cart:
        if item_key.startswith('s_'): # Only allow adjustment for sessions
            if action == 'increase':
                cart[item_key] += 1
            elif action == 'decrease':
                if cart[item_key] > 1:
                    cart[item_key] -= 1
                else:
                    del cart[item_key]
        else:
            # For photos, we can only remove them via this view if needed
            if action == 'remove':
                del cart[item_key]

        request.session['cart'] = cart
    return redirect('view_cart')